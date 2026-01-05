---
type: note
status: done
tags: []
sources:
-
authors:
-
---
**Codewords:** evaluation, offline eval, online eval, golden set, LLM-as-judge, rubric, metric, regression tests, RAG evaluation, RAGAS, faithfulness, context precision, answer relevance, task success rate, context recall, answer correctness, hallucination, retrieval quality, generation quality, human eval, automated eval, evaluation dataset, ground truth

## Why Evaluation for AI Agents

AI agents face unique challenges that make evaluation critical:
- **Hallucinations**: Agents can generate plausible but incorrect information
- **Instability**: Same input can produce different outputs (non-deterministic)
- **Fragile prompts**: Small prompt changes can dramatically affect performance
- **Multi-step failures**: Errors can occur at any step (retrieval, reasoning, tool use)
- **Poor user experience**: Agents might "work" but produce unhelpful or confusing outputs

Without systematic evaluation, you're flying blind: you don't know if changes improve or degrade performance.

### Types of Evaluation

**Offline Evaluation:**
- Run on a fixed dataset (golden set) before deployment
- Fast, repeatable, automated
- Examples: Unit tests, regression tests, benchmark datasets

**Online Evaluation:**
- Monitor performance in production (real user interactions)
- Captures real-world behavior but harder to control
- Examples: User feedback, A/B testing, production metrics

**Human Evaluation:**
- Human judges rate quality (most reliable but expensive)
- Used for high-stakes decisions or when automated metrics fail
- Examples: Expert review, crowd-sourced ratings, user surveys

**Automated Evaluation:**
- LLM-as-judge or rule-based metrics (scalable but may have biases)
- Used for continuous monitoring and regression testing
- Examples: RAGAS metrics, LLM-based scoring, task success rate

**Practice Problem: Classifying Evaluation Questions**

Classify each evaluation question into: **unit eval**, **system/integration eval**, or **online eval**

1. "Does the agent correctly call the weather API when given a weather query?"
2. "What percentage of user queries receive helpful answers?"
3. "Does the agent's final answer match the expected format?"
4. "How often does the agent fail to complete multi-step tasks?"
5. "Does the retrieval component return relevant documents?"
6. "What is the user satisfaction score for the agent in production?"

**Expected Output:**
- Classification for each question (1-6)
- Brief rationale for each classification

## Evaluation Dimensions and Metrics for LLM Apps

### Task Types and Their Metrics

**Classification Tasks:**
- Metrics: Accuracy, Precision, Recall, F1-score
- Example: Sentiment analysis, intent classification

**Generation Tasks:**
- Metrics: BLEU, ROUGE (for reference-based), Perplexity (for language modeling)
- Example: Text summarization, translation
- Note: Reference-based metrics require ground truth; LLM-as-judge is common alternative

**Tool-Use / Agent Tasks:**
- Metrics: Task success rate, Tool call accuracy, Step completion rate
- Example: Multi-step reasoning, API calling agents
- Challenge: Harder to automate; often requires task-specific evaluation

**RAG (Retrieval-Augmented Generation) Tasks:**
- Metrics: Context precision, Context recall, Faithfulness, Answer relevance
- Example: Question answering over documents, chatbots with knowledge base
- Specialized tools: RAGAS, TruLens

### LLM-as-Judge Pattern

Instead of comparing to a reference answer, use another LLM to evaluate quality:

```python
# Example: LLM-as-judge for answer quality
def llm_judge_answer(question: str, answer: str, rubric: str) -> float:
---
 judge_prompt = f"""
 Question: {question}
 Answer: {answer}
 
 Rubric: {rubric}
 
 Rate the answer from 0.0 to 1.0 based on the rubric.
 Return only a number.
 """
 
 response = llm.generate(judge_prompt)
 score = float(response.strip())
 return score

# Usage
score = llm_judge_answer(
 question="What is the capital of France?",
 answer="Paris is the capital of France.",
 rubric="Answer must be factually correct and concise."
)
```

**Risks of LLM-as-Judge:**
- **Bias**: Judge model may favor certain styles or formats
- **Calibration**: Scores may not reflect true quality (over/under-confident)
- **Consistency**: Same answer might get different scores on different runs
- **Cost**: Requires additional LLM calls

**Best Practices:**
- Use clear, specific rubrics
- Calibrate judge scores against human ratings
- Use multiple judge models and average scores
- Consider fine-tuned judge models for domain-specific tasks

**Practice Problem: Designing Metrics for Agent Scenarios**

Design evaluation metrics for these agent scenarios:

**Scenario 1:** Customer support chatbot that answers FAQs from a knowledge base
**Scenario 2:** Research assistant agent that searches the web and synthesizes findings
**Scenario 3:** Code generation agent that writes Python functions based on docstrings

**Tasks:**
1. For each scenario, list 3-5 metrics you would track
2. Specify whether each metric is automated or requires human evaluation
3. For automated metrics, describe how you would compute them (pseudo-code or description)
4. Identify which metrics are most critical for each scenario

**Expected Output:**
- Table or list with scenario → metrics → automation type → computation method
- Rationale for metric selection

## RAG-Specific Evaluation and RAGAS

### RAG Failure Modes

RAG systems can fail in multiple ways:
1. **Bad retrieval**: Wrong documents retrieved, missing relevant documents
2. **Partial context**: Retrieved documents don't fully answer the question
3. **Hallucination over good context**: LLM ignores good context and makes up answers
4. **Poor synthesis**: LLM can't combine information from multiple documents

### RAGAS Metrics Overview

RAGAS (Retrieval-Augmented Generation Assessment) provides specialized metrics for RAG systems:

**Retrieval Metrics:**
- **Context Precision**: Are the retrieved documents relevant? (Precision of retrieval)
- **Context Recall**: Did we retrieve all relevant documents? (Recall of retrieval)

**Generation Metrics:**
- **Faithfulness**: Does the answer stay true to the retrieved context? (No hallucination)
- **Answer Relevance**: Is the answer relevant to the question?
- **Answer Correctness**: Is the answer factually correct? (Requires ground truth)

### RAGAS Input Data Structure

RAGAS expects data in a specific format:

```python
from datasets import Dataset

# Each example needs:
# - question: The user's question
# - contexts: List of retrieved document chunks
# - answer: The generated answer
# - ground_truth: (Optional) The correct answer for correctness metrics

eval_dataset = Dataset.from_dict({
 "question": ["What is the capital of France?"],
 "contexts": [["Paris is the capital of France. It is located in the north-central part of the country."]],
 "answer": ["The capital of France is Paris."],
 "ground_truth": ["Paris"] # Optional, needed for answer_correctness
})
```

### Running RAGAS Evaluation

```python
from ragas import evaluate
from ragas.metrics import (
 faithfulness,
 answer_relevance,
 context_precision,
 context_recall,
 answer_correctness
)

# Prepare dataset (as shown above)
eval_dataset = Dataset.from_dict({
 "question": [
 "What is the capital of France?",
 "Who wrote Romeo and Juliet?"
 ],
 "contexts": [
 ["Paris is the capital of France. It is located in the north-central part of the country."],
 ["Romeo and Juliet is a tragedy written by William Shakespeare in the early part of his career."]
 ],
 "answer": [
 "The capital of France is Paris.",
 "Romeo and Juliet was written by William Shakespeare."
 ],
 "ground_truth": [
 "Paris",
 "William Shakespeare"
 ]
})

# Evaluate with selected metrics
result = evaluate(
 dataset=eval_dataset,
 metrics=[
 faithfulness, # Does answer stay true to context?
 answer_relevance, # Is answer relevant to question?
 context_precision, # Are retrieved contexts relevant?
 context_recall, # Did we retrieve all relevant contexts?
 answer_correctness # Is answer correct? (needs ground_truth)
 ]
)

# Results are a dictionary with metric scores
print(result)
# {
# 'faithfulness': 0.95,
# 'answer_relevance': 0.92,
# 'context_precision': 0.88,
# 'context_recall': 0.75,
# 'answer_correctness': 0.90
# }
```

### Interpreting RAGAS Scores

**Context Precision (0-1):**
- High (0.8+): Retrieved documents are highly relevant
- Low (<0.5): Retrieval is returning irrelevant documents → Fix retriever

**Context Recall (0-1):**
- High (0.8+): Retrieved all relevant documents
- Low (<0.5): Missing relevant documents → Improve retrieval (more documents, better embedding model)

**Faithfulness (0-1):**
- High (0.9+): Answer is faithful to context (no hallucination)
- Low (<0.7): Answer contradicts or adds information not in context → Fix LLM prompt or model

**Answer Relevance (0-1):**
- High (0.8+): Answer directly addresses the question
- Low (<0.6): Answer is generic or off-topic → Improve prompt or post-processing

**Answer Correctness (0-1):**
- High (0.9+): Answer matches ground truth
- Low: Could be due to retrieval, faithfulness, or relevance issues

**Practice Problem: Diagnosing RAG Issues from Metrics**

You have a RAG system with the following RAGAS scores:
- Context Precision: 0.45
- Context Recall: 0.82
- Faithfulness: 0.91
- Answer Relevance: 0.88
- Answer Correctness: 0.65

**Tasks:**
1. Identify the main problem(s) based on these scores
2. What component(s) should you focus on fixing? (Retriever, LLM/prompt, or both)
3. If Context Precision improves to 0.85 but other scores stay the same, what would Answer Correctness likely become? Why?
4. Design an experiment to test your hypothesis about the fix

**Expected Output:**
- Diagnosis of the problem
- Prioritized list of components to fix
- Prediction for Answer Correctness with reasoning
- Experimental plan (hypothesis, what to change, how to measure)

## Other Evaluation Tools and Ecosystem

### DeepEval

DeepEval is an evaluation framework with built-in metrics and test cases:

```python
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric

# Define test case
test_case = LLMTestCase(
 input="What is the capital of France?",
 actual_output="Paris",
 expected_output="Paris",
 context=["Paris is the capital of France."]
)

# Run evaluation
metric = AnswerRelevancyMetric(threshold=0.7)
assert_test(test_case, [metric])
```

**Features:**
- Built-in test assertions (like unit tests)
- Integration with CI/CD pipelines
- Multiple pre-built metrics
- Less specialized for RAG than RAGAS

### TruLens

TruLens provides evaluation with "feedback functions" and explainability:

```python
from trulens_eval import TruChain, Feedback, Huggingface
from trulens_eval.feedback import Groundedness

# Define feedback functions
grounded = Groundedness(groundedness_provider=Huggingface())
f_groundedness = Feedback(grounded.groundedness_measure_with_cot_reasons).on(
 Select.RecordCalls.retriever.get_context().collect(),
 Select.RecordCalls.llm.invoke()
)

# Evaluate chain
tru_chain = TruChain(chain, app_id="rag_app")
tru_chain.on_record(record).run()
```

**Features:**
- Explainability (why did it score this way?)
- Feedback functions for custom metrics
- Good for LangChain integration
- More complex setup than RAGAS

### LangSmith Evals

LangSmith (by LangChain) provides evaluation infrastructure:

```python
from langsmith import Client
from langsmith.evaluation import evaluate

# Define evaluator
def accuracy_evaluator(run, example):
 return {"score": 1 if run.outputs["answer"] == example.outputs["expected"] else 0}

# Run evaluation
results = evaluate(
 lambda inputs: agent.run(inputs["question"]),
 data=eval_dataset,
 evaluators=[accuracy_evaluator],
 experiment_prefix="rag_experiment"
)
```

**Features:**
- Tight integration with LangChain/LangGraph
- Experiment tracking and comparison
- Human feedback collection
- Requires LangSmith account

### Arize Phoenix

Arize Phoenix provides observability and evaluation:

```python
import phoenix as px
from phoenix.evals import run_evals

# Run evaluations
px.launch_app()
run_evals(
 dataframe=eval_df,
 evaluator=your_evaluator,
 output_column="eval_score"
)
```

**Features:**
- Open-source observability platform
- Evaluation capabilities integrated with tracing
- Good for production monitoring
- Less specialized evaluation metrics than RAGAS

### Weights & Biases (W&B) LLM Evaluation

W&B provides experiment tracking with evaluation:

```python
import wandb
from wandb.integration.langchain import WandbTracer

# Track evaluations in W&B
tracer = WandbTracer()
chain.run("query", callbacks=[tracer])
```

**Features:**
- Experiment tracking and visualization
- Integration with many ML frameworks
- Good for comparing model versions
- Less specialized for RAG evaluation

### Choosing the Right Tool

**Use RAGAS when:**
- You're building a RAG system
- You need standard RAG metrics (faithfulness, context precision, etc.)
- You want simple, focused evaluation
- You're doing offline evaluation on datasets

**Use TruLens when:**
- You need explainability (why did it score this way?)
- You're using LangChain and want tight integration
- You want custom feedback functions

**Use LangSmith when:**
- You're heavily invested in LangChain/LangGraph ecosystem
- You need experiment tracking and comparison
- You want human feedback collection

**Use DeepEval when:**
- You want evaluation as "unit tests" (assertions)
- You need CI/CD integration
- You're evaluating non-RAG LLM applications

**Practice Problem: Choosing Evaluation Tools**

For each scenario, recommend the best evaluation tool(s) and justify:

**Scenario A:** RAG-based customer support chatbot, need to evaluate retrieval quality and answer faithfulness
**Scenario B:** LangChain agent with custom tools, need to compare 3 prompt versions in experiments
**Scenario C:** Text classification model, need automated regression tests in CI/CD
**Scenario D:** Multi-modal agent (text + images), need to understand why certain inputs fail

**Tasks:**
1. Recommend primary tool for each scenario (A-D)
2. List 2-3 key features that make it the right choice
3. For Scenario A, show a code snippet of how you'd set up evaluation with your chosen tool

**Expected Output:**
- Tool recommendation for each scenario with rationale
- Code example for Scenario A

## Designing an Evaluation Strategy for Agents

### Defining Success Criteria

Start with product requirements and user needs:

```python
# Example: Success criteria for a research assistant agent
success_criteria = {
 "task_completion_rate": 0.85, # 85% of tasks completed successfully
 "answer_quality_score": 0.80, # Average quality score >= 0.8
 "latency_p95": 10.0, # 95th percentile latency < 10 seconds
 "cost_per_query": 0.05, # Average cost < $0.05 per query
 "user_satisfaction": 4.0 # Average rating >= 4.0/5.0
}
```

### Building a Golden Dataset

A golden dataset (eval set) should:
- Represent real user queries (not synthetic)
- Cover edge cases and failure modes
- Include ground truth when possible
- Be large enough for statistical significance (typically 100-1000 examples)

```python
# Example: Building a golden dataset
import pandas as pd

# Collect real user queries (from production traces or logs)
real_queries = [
 "What is the weather in Paris?",
 "Book a flight to Tokyo",
 "Summarize this document: ...",
 # ... more queries
]

# Add ground truth (manually annotated or from known correct answers)
golden_dataset = pd.DataFrame({
 "question": real_queries,
 "expected_answer": [...], # Ground truth answers
 "expected_tools": [...], # Expected tool calls
 "category": [...], # Query category for analysis
 "difficulty": [...] # Easy/medium/hard
})

# Save for regression testing
golden_dataset.to_json("eval_dataset.json", orient="records")
```

### Combining Automated and Human Evaluation

**Automated evaluation** (for speed and scale):
- Run on every code change (regression tests)
- Monitor production metrics continuously
- Use for A/B testing different versions

**Human evaluation** (for quality and nuance):
- Periodic deep dives (weekly/monthly reviews)
- High-stakes decisions (launching new features)
- Calibrating automated metrics

```python
# Example: Hybrid evaluation strategy
def evaluate_agent(agent, dataset, use_human_eval=False):
 # Always run automated metrics
 automated_scores = {
 "task_success_rate": compute_success_rate(agent, dataset),
 "average_latency": compute_latency(agent, dataset),
 "ragas_scores": run_ragas_evaluation(agent, dataset)
 }
 
 # Optionally run human evaluation on sample
 if use_human_eval:
 sample = dataset.sample(n=50)
 human_scores = collect_human_ratings(agent, sample)
 automated_scores["human_quality_score"] = human_scores
 
 return automated_scores
```

### Regression Testing and CI Integration

Automated evaluation should run in CI/CD:

```python
# Example: Regression test in CI
def test_agent_regression():
 # Load golden dataset
 eval_dataset = load_dataset("eval_dataset.json")
 
 # Run agent on eval set
 results = evaluate_agent(current_agent, eval_dataset)
 
 # Load baseline scores
 baseline_scores = load_baseline_scores()
 
 # Assert no regression
 assert results["task_success_rate"] >= baseline_scores["task_success_rate"] * 0.95
 assert results["answer_quality_score"] >= baseline_scores["answer_quality_score"] * 0.95
 
 # Fail CI if regression detected
 if results["task_success_rate"] < baseline_scores["task_success_rate"]:
 raise AssertionError("Task success rate regressed!")
```

**Practice Problem: Designing Evaluation Plans**

Design evaluation plans for these agents:

**Agent 1:** Customer support chatbot (RAG-based, answers FAQs from knowledge base)
**Agent 2:** Research assistant agent (searches web, synthesizes findings, writes reports)

**Tasks:**
For each agent:
1. Define 3-5 success criteria (with target values)
2. Describe how you would build a golden dataset (source, size, annotation process)
3. Specify which metrics you'd use (automated vs human)
4. Design a regression testing strategy (what to test, when to run, failure thresholds)
5. Describe how you'd monitor performance in production

**Expected Output:**
- Two evaluation plans (one per agent) with all components specified
- Concrete, actionable steps for each component

## Evaluation + Tracing Loop

### Harvesting Traces for Evaluation Datasets

Production traces are a goldmine for building eval datasets:

```python
# Example: Extract eval examples from traces
def harvest_eval_examples_from_traces(traces, min_score=0.8):
 eval_examples = []
 
 for trace in traces:
 # Only use high-quality traces as positive examples
 if trace.scores.get("user_rating", 0) >= min_score:
 eval_examples.append({
 "question": trace.input["query"],
 "contexts": extract_contexts_from_trace(trace),
 "answer": trace.output["answer"],
 "ground_truth": trace.scores.get("expert_rating")
 })
 
 # Use failed traces to identify failure modes
 if trace.status == "error":
 eval_examples.append({
 "question": trace.input["query"],
 "expected_behavior": "should_not_fail",
 "failure_mode": trace.error_message
 })
 
 return eval_examples
```

### Logging Evaluation Scores to Tracing

Attach evaluation scores to traces for monitoring:

```python
from langfuse import Langfuse

langfuse = Langfuse(...)

# Run agent and trace
trace = langfuse.trace(name="agent_query", input={"query": user_query})
result = agent.run(user_query)
trace.update(output={"answer": result})

# Evaluate and attach scores
eval_scores = evaluate_answer(user_query, result, contexts)
trace.score(name="answer_quality", value=eval_scores["quality"])
trace.score(name="faithfulness", value=eval_scores["faithfulness"])
trace.score(name="relevance", value=eval_scores["relevance"])

# Now you can filter traces by evaluation scores in Langfuse
```

### The Complete Feedback Loop

**Observe → Diagnose → Experiment → Evaluate → Deploy**

```python
# 1. OBSERVE: Collect traces from production
production_traces = fetch_traces_from_production(days=7)

# 2. DIAGNOSE: Identify issues
low_quality_traces = filter_traces(production_traces, min_score=0.6)
failure_patterns = analyze_failure_modes(low_quality_traces)
# Example pattern: "Retrieval failing for queries about recent events"

# 3. EXPERIMENT: Try fixes
experiment_traces_v1 = run_agent_with_fix_v1(eval_dataset)
experiment_traces_v2 = run_agent_with_fix_v2(eval_dataset)

# 4. EVALUATE: Compare experiments
scores_v1 = compute_eval_scores(experiment_traces_v1)
scores_v2 = compute_eval_scores(experiment_traces_v2)
if scores_v2["task_success_rate"] > scores_v1["task_success_rate"]:
 best_version = "v2"

# 5. DEPLOY: Ship best version
deploy_agent(best_version)

# 6. Back to OBSERVE: Monitor new version
# (Loop continues)
```

**Practice Problem: Describing the Feedback Loop**

Describe the complete evaluation + tracing feedback loop for a RAG-based customer support chatbot.

**Tasks:**
1. **Observe**: How would you collect data? What would you look for?
2. **Diagnose**: What patterns would indicate problems? How would you identify them?
3. **Experiment**: What experiments would you run? (Give 2-3 concrete examples)
4. **Evaluate**: How would you compare experiments? What metrics?
5. **Deploy**: What criteria would trigger deployment? What would trigger rollback?
6. Show how traces and evaluation scores work together in this loop

**Expected Output:**
- Step-by-step description of the feedback loop
- Concrete examples for each step
- Explanation of how tracing and evaluation integrate

**Key Questions:**

1. What is the difference between offline and online evaluation?
?
- **Offline evaluation**: Run on a fixed dataset (golden set) before deployment; fast, repeatable, automated
- **Online evaluation**: Monitor performance in production with real user interactions; captures real-world behavior but harder to control
- Offline is for pre-deployment testing, online is for production monitoring

2. What are the main failure modes in RAG systems?
?
- **Bad retrieval**: Wrong documents retrieved, missing relevant documents
- **Partial context**: Retrieved documents don't fully answer the question
- **Hallucination over good context**: LLM ignores good context and makes up answers
- **Poor synthesis**: LLM can't combine information from multiple documents

3. What does RAGAS faithfulness measure?
?
- **Faithfulness** measures whether the generated answer stays true to the retrieved context
- High faithfulness (0.9+) means no hallucination (answer doesn't contradict or add information not in context)
- Low faithfulness (<0.7) indicates the LLM is making up information → Fix prompt or model

4. What does RAGAS context precision measure?
?
- **Context precision** measures whether the retrieved documents are relevant to the question
- High precision (0.8+) means retrieved documents are highly relevant
- Low precision (<0.5) means retrieval is returning irrelevant documents → Fix retriever (embedding model, retrieval strategy)

5. What does RAGAS context recall measure?
?
- **Context recall** measures whether all relevant documents were retrieved
- High recall (0.8+) means we retrieved all relevant documents
- Low recall (<0.5) means we're missing relevant documents → Improve retrieval (retrieve more documents, better embedding model)

6. What is LLM-as-judge and what are its risks?
?
- **LLM-as-judge**: Using another LLM to evaluate the quality of answers instead of comparing to ground truth
- **Risks**:
 - Bias: Judge model may favor certain styles or formats
 - Calibration: Scores may not reflect true quality (over/under-confident)
 - Consistency: Same answer might get different scores on different runs
 - Cost: Requires additional LLM calls

7. How do you build a golden dataset for evaluation?
?
- Collect real user queries (from production traces, logs, or user submissions)
- Cover edge cases and failure modes
- Include ground truth when possible (manually annotated or from known correct answers)
- Make it large enough for statistical significance (typically 100-1000 examples)
- Represent real user behavior, not synthetic examples

8. What metrics would you use to evaluate a RAG system?
?
- **Retrieval metrics**: Context precision, Context recall
- **Generation metrics**: Faithfulness, Answer relevance, Answer correctness (if ground truth available)
- **System metrics**: Task success rate, Latency, Cost per query
- Use RAGAS for standard RAG metrics, custom metrics for task-specific evaluation

9. When should you use human evaluation vs automated evaluation?
?
- **Human evaluation**: Periodic deep dives, high-stakes decisions, calibrating automated metrics, when nuance matters
- **Automated evaluation**: Regression tests, continuous monitoring, A/B testing, when scale and speed matter
- Best practice: Combine both (automated for speed/scale, human for quality/calibration)

10. How do you interpret low RAGAS scores to diagnose problems?
?
- **Low context precision**: Fix retriever (better embedding model, retrieval strategy)
- **Low context recall**: Improve retrieval (retrieve more documents, better embedding model)
- **Low faithfulness**: Fix LLM prompt or model (reduce hallucination)
- **Low answer relevance**: Improve prompt or post-processing (make answer more focused)
- **Low answer correctness**: Could be due to any of the above; check all components

11. What is the relationship between tracing and evaluation?
?
- **Tracing** captures execution data (what happened: inputs, outputs, timing, errors)
- **Evaluation** measures quality (how good was the result: scores, metrics)
- Traces can be used to build evaluation datasets (harvest real user queries)
- Evaluation scores can be attached to traces for monitoring
- Together they enable: observe → diagnose → experiment → evaluate → deploy (feedback loop)

12. How would you set up regression testing for an AI agent?
?
- Build a golden dataset (fixed set of test cases with expected outputs)
- Run agent on golden dataset in CI/CD pipeline
- Compare current scores to baseline scores
- Fail CI if scores regress below threshold (e.g., 95% of baseline)
- Update baseline when intentional improvements are made

13. What evaluation tools would you use for a RAG system vs a general LLM application?
?
- **RAG system**: Use RAGAS (specialized RAG metrics: faithfulness, context precision, etc.)
- **General LLM application**: Use DeepEval, TruLens, or LangSmith (more general-purpose metrics)
- Choose based on task type and framework (LangChain → LangSmith/TruLens, pure RAG → RAGAS)

14. How do you handle evaluation when ground truth is not available?
?
- Use **LLM-as-judge** to score quality without ground truth
- Use **reference-free metrics** (e.g., answer relevance, faithfulness in RAGAS)
- Collect **human ratings** on a sample to calibrate automated metrics
- Use **relative evaluation** (compare versions A vs B instead of absolute scores)
- Focus on **task success rate** (did it accomplish the goal?) rather than exact match

15. What is the complete feedback loop for improving an AI agent?
?
- **Observe**: Collect traces from production, identify low-quality outputs
- **Diagnose**: Analyze failure patterns (e.g., "retrieval failing for recent events")
- **Experiment**: Try fixes (different prompts, models, retrieval strategies)
- **Evaluate**: Compare experiments on eval dataset (automated + human)
- **Deploy**: Ship best version, monitor in production
- **Loop**: Continue observing and iterating

16. How do you evaluate multi-step agents (agents that use tools)?
?
- **Task success rate**: Did the agent complete the task correctly?
- **Tool call accuracy**: Were the right tools called with correct parameters?
- **Step completion rate**: How many steps completed successfully?
- **End-to-end evaluation**: Test the complete workflow, not just individual steps
- Use **golden datasets** with expected tool calls and final outputs
- Consider **LLM-as-judge** for complex, subjective tasks

17. What are the trade-offs between different evaluation tools (RAGAS, TruLens, LangSmith)?
?
- **RAGAS**: Simple, focused on RAG metrics, easy to use, less flexible
- **TruLens**: More explainability, good LangChain integration, custom feedback functions, more complex
- **LangSmith**: Tight LangChain integration, experiment tracking, human feedback, requires account
- Choose based on: framework (LangChain?), need for explainability, RAG vs general LLM, budget

18. How would you explain your evaluation strategy in a job interview?
?
- **What**: Offline eval on golden dataset (RAGAS metrics), online monitoring (user feedback, production metrics), regression tests in CI
- **Why**: Catch regressions, optimize performance, ensure quality before deployment
- **How**: Golden dataset from production traces, automated metrics (RAGAS), human eval for calibration, CI integration
- **Challenges**: Building good golden dataset, balancing automated vs human eval, handling non-deterministic outputs
- **Impact**: Reduced production bugs by 40%, faster iteration cycles, confidence in deployments

