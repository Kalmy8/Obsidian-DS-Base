# Migrate to Pydantic State and Refactor Graph Architecture

  

## Overview

  

This plan migrates both `xyber-chat-plugin` and `content-core-sdk` from TypedDict to Pydantic BaseModel for state management, introduces parallel execution for independent nodes, and refactors the monolithic `XyberGraphBuilder` into focused, maintainable components.

  

## Phase 1: Migrate State to Pydantic BaseModel

  

### 1.1 Update `XyberGraphState` in xyber-chat-plugin

  

**File**: [`xyber-chat-plugin/src/xyber_chat_plugin/workflow/state.py`](xyber-chat-plugin/src/xyber_chat_plugin/workflow/state.py)

  

- Convert `XyberGraphState` from `TypedDict` to `BaseModel`

- Use `Annotated[list[AnyMessage], add_messages]` for messages field (LangGraph supports this with Pydantic)

- Add `@computed_field` for `conversation_state` that derives from `intents.hangman_game`

- Set appropriate defaults for all fields

- Ensure backward compatibility with dict access patterns initially

  

**Key changes**:

  

```python

from pydantic import BaseModel, Field, computed_field

from typing import Annotated

from langgraph.graph.message import add_messages

  

class XyberGraphState(BaseModel):

messages: Annotated[list[AnyMessage], add_messages] = Field(default_factory=list)

# Can we define a clear and separate "Input State" for the graph?

# Devs will be happy because it makes things more transparent

user_id: str | None = None

original_query: str | None = None

  

intents: IntentResult | None = None

retrieved_memory: str | None = None

hangman_game_result: str | None = None

hashed_tee_quote: str | None = None

  

# let's actually use nested models for that financial stuff

detected_financial_action: str | None = None

detected_financial_tokens: list[str] | None = None

detected_financial_amounts: list[str] | None = None

detected_financial_blockchains: list[str] | None = None

  
  

response_ready: bool | None = None

@computed_field

@property

def conversation_state(self) -> Literal["conversation", "hangman_game"]:

# I do not love that we only use conversation and hangman game here,

# but do not include tee quote

# I remembre this is because tee quote is like an urgent bid

# And conversation + hangman are indeed long-living states,

# In which our graph performs different....

  

# Maybe we can split hangman in a separate graph then?

# Idk. It seems like instead of having 1 complex multi-state graph

# Which behavies unexpectedly under different circumstances

# It's much better to have separate graphs which are more

# Determenistic and are being picked...

  

"""Derived from intents.hangman_game flag."""

if self.intents and self.intents.hangman_game:

return "hangman_game"

return "conversation"

```

  

### 1.2 Update `BaseGraphState` in content-core-sdk

  

**File**: [`content-core-sdk/content_core_sdk/graph_registry/graphs/base_graph.py`](content-core-sdk/content_core_sdk/graph_registry/graphs/base_graph.py)

  

- Convert `BaseGraphState` from `TypedDict` to `BaseModel`

- Use `Annotated[list[AnyMessage], add_messages]` for messages

- Update `CallableNode` and `BaseGraphBuilder` type hints

- Update `ReActGraphState` to inherit from Pydantic model

  

### 1.3 Update State Access Patterns

  

**Files**: All files using `XyberGraphState` or `BaseGraphState`

  

- Replace `state["key"] `with `state.key` (attribute access)

- Replace `state.get("key")` with `state.key` or `getattr(state, "key", None)`

- Update `state_helpers.py` to work with Pydantic models

- Update all node functions, validators, selectors, and contributors

  

**Affected files**:

  

- `xyber-chat-plugin/src/xyber_chat_plugin/workflow/chat_graph.py`

- `xyber-chat-plugin/src/xyber_chat_plugin/workflow/intents.py`

- `xyber-chat-plugin/src/xyber_chat_plugin/workflow/output_validator.py`

- `xyber-chat-plugin/src/xyber_chat_plugin/workflow/call_llm_policy.py`

- `xyber-chat-plugin/src/xyber_chat_plugin/workflow/llm_selectors.py`

- `xyber-chat-plugin/src/xyber_chat_plugin/workflow/prompt_contributors.py`

- `xyber-chat-plugin/src/xyber_chat_plugin/utils/state_helpers.py`

- `content-core-sdk/content_core_sdk/graph_registry/graphs/react_graph.py`

- `content-core-sdk/content_core_sdk/guardrails_registry/guardrails.py`

  

### 1.4 Handle State Updates in Nodes

  

- Nodes return `dict` updates (LangGraph merges these into Pydantic models)

- Ensure computed fields are recalculated correctly after updates

- Test that `add_messages` reducer works correctly with Pydantic

  

## Phase 2: Refactor Graph Structure for Parallel Execution

  

### 2.1 Analyze Node Dependencies

  

**Current sequential flow** (lines 144-153 in `chat_graph.py`):

  

```

init_node → classify_intent → classify_financial_action_guarded →

retrieve_memory → handle_nft_sale → handle_tee_quote →

prepare_hangman → llm → validate_output

```

  

**Dependency analysis**:

  

- `handle_nft_sale`: Depends on `intents.nft_sale`, `response_ready`

- `handle_tee_quote`: Depends on `intents.tee_quote`, `response_ready`, `hashed_tee_quote`

- `_classify_financial_action_guarded`: Depends on `intents.financial_action`, `original_query`

- `retrieve_memory`: Depends on `user_id`, `original_query`, `response_ready`

  

**Parallelization opportunity**: After `retrieve_memory` and `classify_intent`, `handle_nft_sale`, `handle_tee_quote`, and `_classify_financial_action_guarded` can run in parallel (they're independent).

  

### 2.2 Restructure Graph for Parallel Execution

  

**File**: [`xyber-chat-plugin/src/xyber_chat_plugin/workflow/chat_graph.py`](xyber-chat-plugin/src/xyber_chat_plugin/workflow/chat_graph.py)

  

- Remove `_prepare_hangman` node (replaced by computed property)

- Create a routing node after `retrieve_memory` that fans out to parallel handlers

- Use conditional edges to route to handlers based on intents

- All handlers converge before `llm` node

- Structure:

```

init_node → classify_intent → classify_financial_action_guarded → retrieve_memory

→ [parallel: handle_nft_sale, handle_tee_quote] → llm → validate_output

```

  
  

# let's also remove end_cleanup node as it's redundant and does nothing right now

  

**Implementation**:

  

- Add routing function `_route_to_handlers(state)` that returns list of applicable handlers

- Use `add_conditional_edges` with multiple target nodes for parallel execution

  

# Do not add conditional edges here!!!

  

# I do not love that design

  

# Langgraph suggest you decide when will the node be executed

  

# I love the opposite design: let the nodes decide if they should be

  

# Executed based on the current state

  

# This makes the system more flexible and clear

  

# Conditional edges only needed for loops in my opininon

  

- Ensure handlers are idempotent (check `response_ready` before processing)

  

## Phase 3: Break Down God Object (SRP Refactoring)

  

### 3.1 Extract Node Implementations

  

**Create**: `xyber-chat-plugin/src/xyber_chat_plugin/workflow/nodes/` directory

  

**Extract nodes into separate modules**:

  

# Wow wow wow!

  

# Dont do this, that's overengenerring VERY VERY MUCH

  

# I meant to maybe transfer some fucntionality to a separate semi-graph idk...

  

- `init_node.py`: `InitNode` class

- `memory_node.py`: `MemoryRetrievalNode` class

- `nft_handler.py`: `NftSaleHandlerNode` class

- `tee_handler.py`: `TeeQuoteHandlerNode` class

- `financial_classifier.py`: `FinancialActionClassifierNode` class

- `llm_node.py`: `LlmNode` class

- `memory_saver.py`: `MemorySaverNode` class

- `hangman_finalizer.py`: `HangmanFinalizerNode` class

- `cleanup_node.py`: `CleanupNode` class

  

**Each node class**:

  

- Takes dependencies via `__init__`

- Implements `async def __call__(self, state: XyberGraphState) -> dict`

- Has single responsibility

- Is testable in isolation

  

### 3.2 Extract Graph Builder

  

**Create**: `xyber-chat-plugin/src/xyber_chat_plugin/workflow/graph_builder.py`

  

**New `XyberGraphBuilder` class**:

  

# Nope

  

- Focuses solely on graph construction

- Takes node instances as dependencies

- Builds graph structure using nodes

- No business logic, only orchestration

  

### 3.3 Extract Configuration

  

**Create**: `xyber-chat-plugin/src/xyber_chat_plugin/workflow/config.py`

  

**`GraphConfig` dataclass**:

  

# Nope

  

- Contains all configuration parameters

- Replaces 20+ `__init__` parameters

- Makes dependencies explicit

  

### 3.4 Update Dependencies Module

  

# Nope

  

**File**: [`xyber-chat-plugin/src/xyber_chat_plugin/dependencies.py`](xyber-chat-plugin/src/xyber_chat_plugin/dependencies.py)

  

- Create node instances

- Wire dependencies

- Pass to `XyberGraphBuilder`

- Maintains dependency injection pattern

  

## Phase 4: Update Tests

  

### 4.1 Update State Tests

  

- Test Pydantic model validation

- Test computed field `conversation_state`

- Test `add_messages` reducer with Pydantic

- Test state updates from nodes

  

### 4.2 Update Node Tests

  

- Test each extracted node class independently

- Mock dependencies

- Test parallel execution scenarios

- Test routing logic

  

### 4.3 Update Integration Tests

  

- Test full graph execution

- Test state transitions

- Test parallel handler execution

- Verify backward compatibility

  

## Phase 5: Update Documentation

  

- Update docstrings for Pydantic models

- Document computed fields

- Document parallel execution strategy

- Update architecture diagrams

  

## Implementation Order

  

1. **Phase 1.1-1.2**: Migrate state models to Pydantic (both projects)

2. **Phase 1.3**: Update state access patterns (incremental, file by file)

3. **Phase 1.4**: Verify state updates work correctly

4. **Phase 3.1**: Extract node implementations (enables Phase 2)

5. **Phase 3.2-3.3**: Extract builder and config

6. **Phase 2**: Restructure graph for parallel execution

7. **Phase 4**: Update all tests

8. **Phase 5**: Update documentation

  

## Migration Strategy

  

- **Backward compatibility**: Initially support both dict and attribute access

- **Incremental migration**: Migrate one module at a time

- **Test coverage**: Maintain 100% test coverage during migration

- **Rollback plan**: Keep TypedDict version in git history

  

## Key Benefits

  

1. **Type safety**: Pydantic provides runtime validation

2. **Computed properties**: Derived state automatically calculated

3. **Parallel execution**: Independent handlers run concurrently

4. **Maintainability**: Smaller, focused classes following SRP

5. **Testability**: Nodes can be tested in isolation

6. **Extensibility**: Easier to add new handlers and nodes