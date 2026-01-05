---
type: note
status: done
tags: []
sources:
-
- "[[LangGraph Course]]"
authors:
-
---

# **1) How does `add_messages` reducer work with Annotations?**

### **Key principle:**

LangGraph uses **Python type annotations** as metadata that determines how the state fields should be _reduced_ (merged) when multiple nodes update the same key.

LangGraph calls this system **State Reducers**.

Example:

`from typing_extensions import Annotated import operator class State(TypedDict): messages: Annotated[list[str], operator.add]`

This means:

- The state key `messages` has type `list[str]`
 
- It uses **operator.add** as its reducer
 
- So if multiple nodes return new `messages` lists, LangGraph calls:
 
 `reducer = operator.add state["messages"] = reducer(state["messages"], new_messages)`
 

### ✔️ What reducer Annotations are supported?

LangGraph supports **any callable** reducer—but there are **special built-ins** that LangGraph interprets and uses in special ways.

### **Frequently used built-in reducers**

|Annotation|Means|Notes|
|---|---|---|
|`operator.add`|**append / concatenate**|The most common pattern for "message streams", logs, arrays, etc.|
|`operator.or_`|**merge dicts shallowly**|`{**a, **b}` behavior|
|`operator.and_`|**intersection**|Rare|
|`None` (no annotation)|**replace**|Default behavior: last write wins|
---
|Custom reducer (callable)|custom merge logic|Must accept `(old, new)`|

### **Special LangGraph built-in types (very important!)**

LangChain LangGraph also defines several **message-aware reducers**, like the ones used in the `messages` state.

For example:

- `add_messages`
 
- `append`
 
- `concat`
 
- `reduce_jsonpatch`
 
- `merge_dict`
 

❗**BUT these are not annotations** — they are functions LangGraph uses internally, and you attach them as annotations.

Example:

`from langgraph.graph.message import add_messages class S(TypedDict): messages: Annotated[list, add_messages]`

This reducer:

- understands LangChain `AIMessage`, `HumanMessage`, `SystemMessage`, and `ToolMessage`
 
- merges according to the message protocol
 
- preserves metadata
 
- makes "message graph" workflows work correctly
 

### ✔️ Where to find full list?

LangGraph documents the reducer system here:

**https://docs.langchain.com/oss/python/langgraph/use-graph-api#reducers**

**and the message reducer options here:**

**https://docs.langchain.com/oss/python/langgraph/messages**

The public reducers include:

- `add_messages`
- `append`
- `concat`
- `merge_dict`
- `reduce_jsonpatch`