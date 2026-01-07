---
type: note
status: done
tags:
- tech/stack/deepeval
sources:
- null
authors:
- null
---
# Conversational Goldens vs Simple Goldens

## Overview

DeepEval supports two types of goldens for different evaluation scenarios:


## Structure Differences

### **Simple Golden (`Golden`)**

**Structure:**
```python
from deepeval.dataset import Golden

golden = Golden(
    input="What is Python?",           # Single input query
    expected_output="Python is a programming language."  # Expected response
)
```

**Contains:**
- `input`: Single prompt/query
- `expected_output`: Expected response to that input
- `context`: Optional context (for RAG)
- `comments`: Optional annotations

**Use Case:** Single-turn Q&A, RAG systems, simple queries

---

### **Conversational Golden (`ConversationalGolden`)**

**Structure:**
```python
from deepeval.dataset import ConversationalGolden

conversational_golden = ConversationalGolden(
    scenario="Frustrated user asking for a refund",  # Conversation scenario
    expected_outcome="Redirect user to a real human agent",  # Desired end result
    user_description="Andy Byron is the CEO of Astronomer"  # User persona
)
```

**Contains:**
- `scenario`: Description of the conversation scenario (not exact inputs)
- `expected_outcome`: Desired end result/goal
- `user_description`: User persona/characteristics

**Key Difference:** No predefined `input`/`expected_output` pairs. Instead, defines a scenario and expected outcome.

**Use Case:** Multi-turn conversations, chatbots, conversational agents

---

## Test Case Differences

### **Simple: `LLMTestCase`**

**Structure:**
```python
from deepeval.test_case import LLMTestCase

test_case = LLMTestCase(
    input="What is Python?",
    actual_output="Python is a programming language.",
    expected_output="Python is a programming language.",
    retrieval_context=["context1", "context2"]  # Optional
)
```

**Contains:**
- `input`: Single query
- `actual_output`: LLM's response
- `expected_output`: Expected response
- `retrieval_context`: Optional context (for RAG metrics)

**Evaluation:** Metrics evaluate single input-output pair

---

### **Conversational: `ConversationalTestCase`**

**Structure:**
```python
from deepeval.test_case import ConversationalTestCase, Turn

conversational_test_case = ConversationalTestCase(
    scenario="Frustrated user asking for a refund",
    expected_outcome="Redirect user to a real human agent",
    user_description="Andy Byron is the CEO of Astronomer",
    turns=[
        Turn(role="user", content="Hello, I want a refund"),
        Turn(role="assistant", content="I understand you'd like a refund..."),
        Turn(role="user", content="This is unacceptable!"),
        Turn(role="assistant", content="Let me connect you with a human agent..."),
    ]
)
```

**Contains:**
- `scenario`: Conversation scenario (from ConversationalGolden)
- `expected_outcome`: Desired outcome (from ConversationalGolden)
- `user_description`: User persona (from ConversationalGolden)
- `turns`: List of `Turn` objects representing the conversation flow
  - Each `Turn` has `role` ("user" or "assistant") and `content`

**Evaluation:** Metrics evaluate entire conversation flow, context retention, coherence

---

## EvaluationDataset Handling

### **Same Dataset Object**

**Yes, `EvaluationDataset` handles both types:**

```python
from deepeval.dataset import EvaluationDataset, Golden, ConversationalGolden

dataset = EvaluationDataset()

# Add simple goldens
dataset.goldens.append(Golden(
    input="What is Python?",
    expected_output="Python is a programming language."
))

# Add conversational goldens
dataset.goldens.append(ConversationalGolden(
    scenario="User asking for help",
    expected_outcome="Issue resolved",
    user_description="New user"
))

# Both stored in dataset.goldens list
print(len(dataset.goldens))  # 2
```

**Important:** The `dataset.goldens` list can contain both `Golden` and `ConversationalGolden` objects mixed together.

---

## Test Case Generation

### **Simple Goldens → LLMTestCase**

**Direct conversion:**
```python
from deepeval.dataset import Golden
from deepeval.test_case import LLMTestCase

golden = Golden(input="What is Python?", expected_output="...")

# Invoke LLM app
actual_output = llm_app(golden.input)

# Create test case directly
test_case = LLMTestCase(
    input=golden.input,
    actual_output=actual_output,
    expected_output=golden.expected_output
)
```

**Process:** Simple 1:1 mapping - one golden → one test case

---

### **Conversational Goldens → ConversationalTestCase**

**Requires simulation:**
```python
from deepeval.dataset import ConversationalGolden
from deepeval.test_case import ConversationalTestCase
from deepeval.synthesizer import ConversationSimulator

conversational_golden = ConversationalGolden(
    scenario="User asking for refund",
    expected_outcome="Redirect to human agent",
    user_description="Frustrated customer"
)

# Simulate conversation turns
simulator = ConversationSimulator()
conversational_test_case = simulator.simulate(
    goldens=[conversational_golden],
    max_turns=10
)[0]  # Returns list of ConversationalTestCase

# conversational_test_case now has populated turns
```

**Process:** 
1. ConversationalGolden defines scenario (not exact turns)
2. `ConversationSimulator` generates actual conversation turns
3. Creates `ConversationalTestCase` with simulated `turns`

**Why Simulation?**
- Conversations are dynamic - exact turns can't be predefined
- Simulator generates realistic conversation flow based on scenario
- Allows testing of conversation quality, not just exact matches

---

## Metrics Computation

### **Simple Goldens: Single-Turn Metrics**

**Metrics evaluate individual input-output pairs:**

```python
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric

metric = AnswerRelevancyMetric(threshold=0.7)

# Evaluates: Is the output relevant to the input?
score = metric.measure(test_case)
# Compares: input vs actual_output
```

**Common Metrics:**
- `AnswerRelevancyMetric`: Relevance of answer to query
- `FaithfulnessMetric`: Is answer supported by context?
- `ContextualRelevancyMetric`: Is context relevant?
- `ExactMatchMetric`: Exact string match
- `GEval`: Custom criteria evaluation

**Computation:**
- Takes single `LLMTestCase`
- Compares `actual_output` vs `expected_output`
- Considers `input` and `retrieval_context` (if applicable)
- Returns single score (0.0-1.0)

---

### **Conversational Goldens: Multi-Turn Metrics**

**Metrics evaluate entire conversation flow:**

```python
from deepeval.metrics import TurnRelevancyMetric, ConversationalGEval

metric = TurnRelevancyMetric(threshold=0.7)

# Evaluates: Is each turn relevant in conversation context?
score = metric.measure(conversational_test_case)
# Compares: Each turn's relevance to conversation flow
```

**Common Metrics:**
- `TurnRelevancyMetric`: Relevance of each turn to conversation
- `ConversationalGEval`: Custom criteria for entire conversation
- `ConversationalDAGMetric`: Custom decision-tree evaluation
- `GoalAccuracyMetric`: Did conversation achieve goal?

**Computation:**
- Takes `ConversationalTestCase` with multiple `turns`
- Evaluates:
  - **Per-turn**: Relevance of each turn
  - **Conversation-level**: Coherence, context retention, goal achievement
- Considers conversation history/context
- Returns score for entire conversation (0.0-1.0)

**Key Difference:** Metrics consider conversation context, not just individual turns

---

## Evaluation Flow Comparison

### **Simple Goldens Flow**

```
Golden (input + expected_output)
    ↓
[Invoke LLM App]
    ↓
LLMTestCase (input + actual_output + expected_output)
    ↓
[Apply Metrics]
    ↓
Score (single value)
```

**Example:**
```python
golden = Golden(input="What is Python?", expected_output="...")
actual_output = llm_app(golden.input)
test_case = LLMTestCase(
    input=golden.input,
    actual_output=actual_output,
    expected_output=golden.expected_output
)
evaluate(test_cases=[test_case], metrics=[AnswerRelevancyMetric()])
```

---

### **Conversational Goldens Flow**

```
ConversationalGolden (scenario + expected_outcome)
    ↓
[ConversationSimulator.simulate()]
    ↓
ConversationalTestCase (scenario + turns + expected_outcome)
    ↓
[Apply Conversational Metrics]
    ↓
Score (conversation-level value)
```

**Example:**
```python
conversational_golden = ConversationalGolden(
    scenario="User asking for refund",
    expected_outcome="Redirect to agent"
)

# Simulate conversation
simulator = ConversationSimulator()
conversational_test_case = simulator.simulate(
    goldens=[conversational_golden],
    max_turns=10
)[0]

# Evaluate conversation
evaluate(
    conversational_test_cases=[conversational_test_case],
    metrics=[TurnRelevancyMetric()]
)
```

---

## Key Differences Summary

| Aspect | Simple Goldens | Conversational Goldens |
|--------|---------------|------------------------|
| **Golden Type** | `Golden` | `ConversationalGolden` |
| **Structure** | `input` + `expected_output` | `scenario` + `expected_outcome` |
| **Test Case** | `LLMTestCase` | `ConversationalTestCase` |
| **Test Case Contains** | Single input-output pair | Multiple `Turn` objects |
| **Generation** | Direct (1:1 mapping) | Requires `ConversationSimulator` |
| **Metrics** | Single-turn metrics | Multi-turn/conversational metrics |
| **Evaluation Focus** | Individual Q&A quality | Conversation flow, coherence, context |
| **Use Case** | RAG, Q&A, single queries | Chatbots, conversational agents |

---

## When to Use Each

### **Use Simple Goldens (`Golden`) When:**
- ✅ Single-turn Q&A systems
- ✅ RAG pipelines
- ✅ Information retrieval
- ✅ Simple query-response pairs
- ✅ You have exact input-output pairs

**Example:**
```python
golden = Golden(
    input="What is the capital of France?",
    expected_output="Paris"
)
```

---

### **Use Conversational Goldens (`ConversationalGolden`) When:**
- ✅ Multi-turn conversations
- ✅ Chatbots and conversational agents
- ✅ Context-dependent interactions
- ✅ Goal-oriented dialogues
- ✅ You care about conversation flow, not exact matches

**Example:**
```python
conversational_golden = ConversationalGolden(
    scenario="Customer service interaction",
    expected_outcome="Customer issue resolved",
    user_description="Frustrated customer with billing issue"
)
```

---

## Code Examples

### **Simple Golden Evaluation**

```python
import pytest
from deepeval import assert_test
from deepeval.dataset import Golden, EvaluationDataset
from deepeval.tracing import observe
from deepeval.metrics import AnswerRelevancyMetric

dataset = EvaluationDataset()
dataset.add_goldens_from_csv_file(
    file_path="./qa_dataset.csv",
    input_col_name="question",
    expected_output_col_name="answer"
)

@observe(metrics=[AnswerRelevancyMetric(threshold=0.7)])
def qa_app(question: str) -> str:
    # Your Q&A logic
    return "answer"

@pytest.mark.parametrize("golden", dataset.goldens)
def test_qa(golden: Golden):
    assert_test(golden=golden, observed_callback=qa_app)
```

---

### **Conversational Golden Evaluation**

```python
import pytest
from deepeval import evaluate
from deepeval.dataset import ConversationalGolden, EvaluationDataset
from deepeval.test_case import ConversationalTestCase
from deepeval.metrics import TurnRelevancyMetric
from deepeval.synthesizer import ConversationSimulator

dataset = EvaluationDataset()
dataset.goldens = [
    ConversationalGolden(
        scenario="User asking for refund",
        expected_outcome="Redirect to human agent",
        user_description="Frustrated customer"
    ),
    # ... more conversational goldens
]

# Simulate conversations
simulator = ConversationSimulator()
conversational_test_cases = simulator.simulate(
    goldens=dataset.goldens,
    max_turns=10
)

# Evaluate conversations
evaluate(
    conversational_test_cases=conversational_test_cases,
    metrics=[TurnRelevancyMetric(threshold=0.7)]
)
```

---

## Important Notes

1. **Same EvaluationDataset**: Both types can coexist in the same dataset
2. **Different Test Cases**: `LLMTestCase` vs `ConversationalTestCase` - cannot mix in same evaluation
3. **Different Metrics**: Use single-turn metrics for `LLMTestCase`, conversational metrics for `ConversationalTestCase`
4. **Simulation Required**: Conversational goldens need `ConversationSimulator` to generate actual turns
5. **Evaluation Separately**: Evaluate simple and conversational test cases in separate calls to `evaluate()` or `assert_test()`

---

## References

- [DeepEval End-to-End Evals](https://deepeval.com/docs/evaluation-end-to-end-llm-evals)
- [Multi-Turn Evals](https://deepeval.com/docs/evaluation-end-to-end-llm-evals#multi-turn-e2e-evals)
- [Conversational Metrics](https://deepeval.com/docs/metrics-conversational)
- [Conversation Simulator](https://deepeval.com/docs/synthetic-data-generation-conversation-simulator)


