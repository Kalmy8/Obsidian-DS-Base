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
# DeepEval Metrics Guide

## Overview

DeepEval provides a comprehensive suite of metrics to evaluate LLM applications. Metrics use **LLM-as-a-judge** approach (typically GPT-4) to assess outputs. This guide covers the most popular metrics, what they measure, and how to tune them.


## RAG Metrics

### **AnswerRelevancyMetric**

**What It Measures:**
- How relevant the generated answer is to the input query
- Whether the answer addresses the question asked
- Semantic similarity between query and answer

**Use Case:** RAG QA systems, chatbots, information retrieval

**Tuning:**
```python
from deepeval.metrics import AnswerRelevancyMetric

metric = AnswerRelevancyMetric(
    threshold=0.7,  # Minimum passing score (0.0-1.0)
    model="gpt-4.1"  # Judge model for evaluation
)
```

**Parameters:**
- `threshold` (float, default: 0.5): Minimum score to pass. Higher = stricter
- `model` (str): LLM model used as judge (default: "gpt-4.1")

**When to Adjust:**
- Lower threshold (0.3-0.5): More lenient, accepts partially relevant answers
- Higher threshold (0.7-0.9): Stricter, requires highly relevant answers

---

### **FaithfulnessMetric**

**What It Measures:**
- Whether the answer is supported by the provided context
- Detects hallucinations (claims not in context)
- Factual consistency with retrieval context

**Use Case:** RAG systems where accuracy is critical

**Tuning:**
```python
from deepeval.metrics import FaithfulnessMetric

metric = FaithfulnessMetric(
    threshold=0.8,  # Stricter for factual accuracy
    model="gpt-4.1"
)
```

**Parameters:**
- `threshold` (float, default: 0.5): Minimum passing score
- `model` (str): Judge model

**When to Adjust:**
- Lower threshold (0.3-0.5): Allows some inference/interpretation
- Higher threshold (0.8-0.9): Strict factual accuracy required

**Note:** Requires `retrieval_context` in `LLMTestCase`

---

### **ContextualRelevancyMetric**

**What It Measures:**
- Whether the retrieved context is relevant to the query
- Quality of retrieval component in RAG pipeline
- Proportion of relevant context retrieved

**Use Case:** Evaluating retrieval systems, RAG pipeline optimization

**Tuning:**
```python
from deepeval.metrics import ContextualRelevancyMetric

metric = ContextualRelevancyMetric(
    threshold=0.6,
    model="gpt-4.1"
)
```

**Parameters:**
- `threshold` (float, default: 0.5): Minimum passing score
- `model` (str): Judge model

**When to Adjust:**
- Lower threshold: Accepts broader context retrieval
- Higher threshold: Requires highly focused context

**Note:** Requires `retrieval_context` in `LLMTestCase`

---

### **RAGAS Metric** (Composite)

**What It Measures:**
Averaged score of four RAG metrics:
- Answer Relevancy
- Faithfulness
- Contextual Precision
- Contextual Recall

**Use Case:** Holistic RAG pipeline evaluation

**Tuning:**
```python
from deepeval.metrics.ragas import RagasMetric

metric = RagasMetric(
    threshold=0.5,  # Overall passing score
    model="gpt-3.5-turbo"  # Can use cheaper model for RAGAS
)
```

**Parameters:**
- `threshold` (float, default: 0.5): Minimum average score
- `model` (str): Judge model (can use cheaper models)

**When to Use:**
- Quick overall RAG assessment
- Comparing different RAG configurations
- CI/CD pipelines

---

## Agent Metrics

### **ToolCorrectnessMetric**

**What It Measures:**
- Whether correct tools were called
- Accuracy of tool arguments
- Correctness of tool usage sequence

**Use Case:** LLM agents with function calling, tool-using systems

**Tuning:**
```python
from deepeval.metrics import ToolCorrectnessMetric
from deepeval.metrics.tool_correctness import ToolCallParams

metric = ToolCorrectnessMetric(
    available_tools=["WebSearch", "Calculator", "DatabaseQuery"],
    threshold=0.7,
    evaluation_params=[
        ToolCallParams.TOOL_NAME,
        ToolCallParams.INPUT_PARAMETERS,
        ToolCallParams.OUTPUT
    ],
    should_consider_ordering=False,  # Order doesn't matter
    should_exact_match=False,  # Allow partial matches
    strict_mode=False  # Binary scoring (1 or 0)
)
```

**Parameters:**
- `available_tools` (list): All tools available to agent
- `threshold` (float, default: 0.5): Minimum passing score
- `evaluation_params` (list): What to evaluate (tool name, args, output)
- `should_consider_ordering` (bool): Whether tool call order matters
- `should_exact_match` (bool): Require exact matches
- `strict_mode` (bool): Binary scoring (1 or 0)

**When to Adjust:**
- `strict_mode=True`: Pass/fail only, no partial credit
- `should_exact_match=True`: Tools must match exactly
- `evaluation_params`: Control what aspects are evaluated

---

### **GoalAccuracyMetric**

**What It Measures:**
- Agent's ability to plan tasks
- Execution adherence to plan
- Goal completion accuracy

**Use Case:** Multi-turn agent interactions, task-oriented agents

**Tuning:**
```python
from deepeval.metrics import GoalAccuracyMetric

metric = GoalAccuracyMetric(
    threshold=0.6,
    model="gpt-4o",
    strict_mode=False
)
```

**Parameters:**
- `threshold` (float, default: 0.5): Minimum passing score
- `model` (str, default: "gpt-4o"): Judge model
- `strict_mode` (bool): Binary scoring

**When to Use:**
- Evaluating agent workflows
- Multi-step task completion
- Planning vs execution assessment

**Note:** Requires `ConversationalTestCase` with `turns`

---

## Safety & Compliance Metrics

### **BiasMetric**

**What It Measures:**
- Gender bias in outputs
- Racial bias
- Political bias
- Fairness and neutrality

**Use Case:** Ensuring ethical AI, compliance requirements

**Tuning:**
```python
from deepeval.metrics import BiasMetric

metric = BiasMetric(
    threshold=0.3,  # Lower = more sensitive to bias
    model="gpt-4.1"
)
```

**Parameters:**
- `threshold` (float, default: 0.5): Lower = more sensitive
- `model` (str): Judge model

**When to Adjust:**
- Lower threshold (0.2-0.3): Catch subtle biases
- Higher threshold (0.6-0.7): Only flag obvious bias

---

### **NonAdviceMetric**

**What It Measures:**
- Presence of inappropriate professional advice
- Compliance with regulatory restrictions
- Avoidance of unauthorized guidance

**Use Case:** Financial chatbots, medical assistants, legal advisors

**Tuning:**
```python
from deepeval.metrics import NonAdviceMetric

metric = NonAdviceMetric(
    threshold=0.5,  # Lower = stricter (flags more as advice)
    model="gpt-4.1"
)
```

**Parameters:**
- `threshold` (float, default: 0.5): Lower = stricter detection
- `model` (str): Judge model

**When to Adjust:**
- Lower threshold: More conservative, flags borderline cases
- Higher threshold: Only flags clear advice violations

---

### **MisuseMetric**

**What It Measures:**
- Whether chatbot is used outside intended domain
- Scope violations
- Inappropriate usage detection

**Use Case:** Domain-specific chatbots, specialized assistants

**Tuning:**
```python
from deepeval.metrics import MisuseMetric

metric = MisuseMetric(
    domain="financial",  # Specify chatbot domain
    threshold=0.5,
    model="gpt-4.1"
)
```

**Parameters:**
- `domain` (str): Intended domain (e.g., "financial", "medical")
- `threshold` (float, default: 0.5): Detection sensitivity
- `model` (str): Judge model

**When to Adjust:**
- Lower threshold: More sensitive to misuse
- Higher threshold: Only flag clear misuse

---

### **PIILeakageMetric**

**What It Measures:**
- Presence of Personally Identifiable Information
- GDPR/CCPA/HIPAA compliance
- Privacy violations

**Use Case:** Customer-facing applications, healthcare systems

**Tuning:**
```python
from deepeval.metrics import PIILeakageMetric

metric = PIILeakageMetric(
    threshold=0.3  # Lower = more sensitive
)
```

**Parameters:**
- `threshold` (float): Lower = more sensitive detection

**When to Adjust:**
- Very low threshold (0.1-0.2): Maximum privacy protection
- Higher threshold: Only flag obvious PII

---

### **ToxicityMetric**

**What It Measures:**
- Offensive or harmful content
- Toxic language detection
- Content safety

**Use Case:** Public-facing chatbots, content moderation

**Tuning:**
```python
from deepeval.metrics import ToxicityMetric

metric = ToxicityMetric(
    threshold=0.3  # Lower = stricter
)
```

**Parameters:**
- `threshold` (float): Lower = stricter detection

**When to Adjust:**
- Lower threshold: More conservative content filtering
- Higher threshold: Only flag severe toxicity

---

## Format & Structure Metrics

### **ExactMatchMetric**

**What It Measures:**
- Exact string match between actual and expected output
- Perfect precision required

**Use Case:** Translation, code generation, structured outputs

**Tuning:**
```python
from deepeval.metrics import ExactMatchMetric

metric = ExactMatchMetric(
    threshold=1.0,  # Must be exact match
    verbose_mode=True  # Show comparison details
)
```

**Parameters:**
- `threshold` (float, default: 1.0): Must be 1.0 for exact match
- `verbose_mode` (bool): Show detailed comparison

**When to Use:**
- Translation tasks
- Code generation
- Any task requiring exact output

---

### **PatternMatchMetric**

**What It Measures:**
- Whether output matches regex pattern
- Format compliance
- Structure validation

**Use Case:** Email extraction, phone numbers, structured formats

**Tuning:**
```python
from deepeval.metrics import PatternMatchMetric

metric = PatternMatchMetric(
    pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$",  # Email regex
    ignore_case=False,  # Case-sensitive
    threshold=1.0,  # Must match pattern
    verbose_mode=True
)
```

**Parameters:**
- `pattern` (str): Regular expression pattern
- `ignore_case` (bool, default: False): Case sensitivity
- `threshold` (float, default: 1.0): Must match pattern
- `verbose_mode` (bool): Show matching details

**When to Use:**
- Format validation
- Structured data extraction
- Output format requirements

---

### **JsonCorrectnessMetric**

**What It Measures:**
- JSON schema compliance
- Valid JSON structure
- Schema adherence

**Use Case:** API responses, structured data generation

**Tuning:**
```python
from pydantic import BaseModel
from deepeval.metrics import JsonCorrectnessMetric

class UserSchema(BaseModel):
    name: str
    age: int
    email: str

metric = JsonCorrectnessMetric(
    schema=UserSchema,
    threshold=1.0,  # Must be valid JSON matching schema
    verbose_mode=True
)
```

**Parameters:**
- `schema` (BaseModel): Pydantic schema definition
- `threshold` (float, default: 1.0): Must match schema
- `verbose_mode` (bool): Show validation errors

**When to Use:**
- API response validation
- Structured output generation
- Schema compliance

---

## Conversational Metrics

### **TurnRelevancyMetric**

**What It Measures:**
- Relevance of each turn in conversation
- Contextual appropriateness
- Multi-turn coherence

**Use Case:** Chatbots, conversational agents

**Tuning:**
```python
from deepeval.metrics import TurnRelevancyMetric

metric = TurnRelevancyMetric(
    threshold=0.6,
    model="gpt-4.1"
)
```

**Parameters:**
- `threshold` (float, default: 0.5): Minimum relevancy score
- `model` (str): Judge model

**Note:** Requires `ConversationalTestCase` with `turns`

---

### **ConversationalDAGMetric**

**What It Measures:**
- Custom evaluation using decision trees
- Complex multi-turn assessment
- User-defined evaluation logic

**Use Case:** Complex conversational flows, custom evaluation criteria

**Tuning:**
```python
from deepeval.metrics import ConversationalDAGMetric
from deepeval.metrics.conversational_dag import DeepAcyclicGraph, Node

# Define custom DAG
dag = DeepAcyclicGraph(
    nodes=[
        Node(id="start", condition="..."),
        Node(id="check_intent", condition="..."),
        # ... more nodes
    ]
)

metric = ConversationalDAGMetric(
    dag=dag,
    threshold=0.5,
    model="gpt-4.1",
    strict_mode=False
)
```

**Parameters:**
- `dag` (DeepAcyclicGraph): Custom decision tree
- `threshold` (float, default: 0.5): Minimum passing score
- `model` (str): Judge model
- `strict_mode` (bool): Binary scoring

**When to Use:**
- Custom evaluation workflows
- Complex conversational logic
- Domain-specific criteria

---

## Custom Metrics

### **GEval** (Generic LLM Evaluation)

**What It Measures:**
- User-defined evaluation criteria
- Chain-of-thought evaluation
- Flexible assessment framework

**Use Case:** Custom evaluation needs, subjective criteria

**Tuning:**
```python
from deepeval.metrics import GEval

metric = GEval(
    criteria="Coherence and relevance of the response",
    evaluation_steps=[
        "Assess if the response is coherent",
        "Evaluate relevance to the query",
        "Check for logical flow"
    ],
    model="gpt-4.1"
)
```

**Parameters:**
- `criteria` (str): Evaluation criteria description
- `evaluation_steps` (list): Step-by-step evaluation process
- `model` (str): Judge model

**When to Use:**
- Custom evaluation needs
- Subjective quality assessment
- Domain-specific criteria

---

## General Tuning Guidelines

### **Threshold Selection**

- **0.0-0.3**: Very lenient, accepts most outputs
- **0.4-0.6**: Balanced, standard use case
- **0.7-0.9**: Strict, high-quality requirements
- **1.0**: Perfect match required (exact match, pattern match)

### **Model Selection**

- **gpt-4.1 / gpt-4**: Highest quality, most expensive
- **gpt-3.5-turbo**: Good balance, cheaper
- **gpt-4o**: Fast, good for high-volume evaluations

### **Common Patterns**

```python
# RAG Pipeline (Recommended)
metrics = [
    AnswerRelevancyMetric(threshold=0.7),
    FaithfulnessMetric(threshold=0.8),
    ContextualRelevancyMetric(threshold=0.6)
]

# Agent System
metrics = [
    ToolCorrectnessMetric(threshold=0.7, strict_mode=False),
    GoalAccuracyMetric(threshold=0.6)
]

# Safety-Critical Application
metrics = [
    BiasMetric(threshold=0.3),
    NonAdviceMetric(threshold=0.4),
    PIILeakageMetric(threshold=0.2)
]
```

---

## References

- [DeepEval Metrics Documentation](https://deepeval.com/docs/eval-metrics)
- [RAG Metrics](https://deepeval.com/docs/metrics-ragas)
- [Agent Metrics](https://deepeval.com/docs/metrics-agentic)
- [Safety Metrics](https://deepeval.com/docs/metrics-safety)




