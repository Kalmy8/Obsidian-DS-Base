---
type: note
status: done
tags: []
sources:
-
authors:
-
---
# DeepEval Framework FAQ

## 1. How should I upload my .csv dataset (turn it into an EvaluationDataset)?

To convert a `.csv` file into an `EvaluationDataset` in DeepEval, follow these steps:

### Step 1: Prepare Your CSV File

Ensure your CSV file includes the necessary columns:

### Step 2: Load CSV into EvaluationDataset

Use the `add_goldens_from_csv_file` method:

```python
from deepeval.dataset import EvaluationDataset

dataset = EvaluationDataset()
dataset.add_goldens_from_csv_file(
    file_path="./your_dataset.csv",  # Absolute path to your CSV file
    input_col_name="input",  # Column name containing inputs
    expected_output_col_name="expected_output",  # Column name containing expected outputs
    context_col_name="context",  # Optional: column name for context
    context_col_delimiter="|"  # Optional: delimiter if context is a delimited string
)
```

**Note**: Replace the column names (`"input"`, `"expected_output"`, `"context"`) with the actual column names in your CSV file.

### Step 3: Save or Push the Dataset

After loading, you can store the dataset for later use:

**Option A: Save Locally**
```python
# Save as JSON
dataset.save_as(
    file_type="json",
    directory="./example"
)

# Save as CSV
dataset.save_as(
    file_type="csv",
    directory="./example"
)
```

**Option B: Push to Confident AI**
```python
dataset.push(alias="My dataset")
```

**Option C: Load from Local File Later**
```python
dataset = EvaluationDataset()
dataset.load_from_file("your_dataset.json")  # Load from JSON
# or
dataset.add_goldens_from_csv_file(...)  # Load from CSV again
```

### Verification

You can verify the dataset was loaded correctly:

```python
print(f"Loaded {len(dataset.goldens)} goldens")
for golden in dataset.goldens[:3]:  # Print first 3
    print(f"Input: {golden.input}")
    print(f"Expected Output: {golden.expected_output}")
```

**Reference**: [DeepEval Datasets Documentation](https://deepeval.com/docs/evaluation-datasets)


## 2. How should I launch the evaluation process with pytest? Should I parametrize a single method to create test cases for each object inside the EvaluationDataset?

Yes, you should parametrize a single test method to iterate over each `Golden` in your `EvaluationDataset`. Here's how:

### Step 1: Load Your Dataset

```python
from deepeval.dataset import EvaluationDataset

# Load from CSV
dataset = EvaluationDataset()
dataset.add_goldens_from_csv_file(
    file_path="./your_dataset.csv",
    input_col_name="input",
    expected_output_col_name="expected_output"
)

# OR load from Confident AI
dataset.pull(alias="your_dataset_alias")

# OR load from local JSON
dataset.load_from_file("your_dataset.json")
```

### Step 2: Define Your LLM Application Function

```python
def llm_app(input_text: str) -> str:
    # Your LLM application logic here
    # This function should take input and return the actual output
    return "Generated output"
```

### Step 3: Create Parametrized Test Function

Use `@pytest.mark.parametrize` to create a test case for each `Golden`:

```python
import pytest
from deepeval import assert_test
from deepeval.dataset import Golden

@pytest.mark.parametrize("golden", dataset.goldens)
def test_llm_app(golden: Golden):
    assert_test(
        golden=golden,
        observed_callback=llm_app
    )
```

**Key Points**:
- `assert_test` automatically invokes `llm_app(golden.input)` to get the actual output
- It compares `actual_output` against `golden.expected_output`
- Each `Golden` in the dataset becomes a separate pytest test case

### Step 4: Run Tests with DeepEval CLI

Execute the tests using the DeepEval CLI (not regular pytest):

```bash
deepeval test run test_llm_app.py
```

This command:
- Runs all parametrized tests
- Generates evaluation reports
- Logs results to Confident AI (if configured)

### Alternative: Using Metrics Explicitly

If you want to specify metrics explicitly in `assert_test`:

```python
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric

@pytest.mark.parametrize("golden", dataset.goldens)
def test_llm_app(golden: Golden):
    assert_test(
        golden=golden,
        observed_callback=llm_app,
        metrics=[AnswerRelevancyMetric(), FaithfulnessMetric()]
    )
```

**Reference**: [DeepEval Unit Testing in CI/CD Documentation](https://deepeval.com/docs/evaluation-unit-testing-in-ci-cd)

---

## 3. How should I instantiate the judge model?

In DeepEval, the "judge model" refers to the **evaluation metrics** used to assess your LLM's performance. Metrics are the components that evaluate test cases.

### Step 1: Import and Instantiate Metrics

DeepEval provides various built-in metrics. Import and instantiate them:

```python
from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric,
    ContextualRelevancyMetric,
    # ... other metrics
)

# Instantiate metrics
relevancy_metric = AnswerRelevancyMetric()
faithfulness_metric = FaithfulnessMetric()
```

### Step 2: Use Metrics in Evaluation

**Option A: With `assert_test` (pytest)**

```python
from deepeval import assert_test

@pytest.mark.parametrize("golden", dataset.goldens)
def test_llm_app(golden: Golden):
    assert_test(
        golden=golden,
        observed_callback=llm_app,
        metrics=[relevancy_metric, faithfulness_metric]
    )
```

**Option B: With `evaluate` (end-to-end evals)**

```python
from deepeval import evaluate
from deepeval.test_case import LLMTestCase

# Create test cases from goldens
test_cases = []
for golden in dataset.goldens:
    actual_output = llm_app(golden.input)
    test_case = LLMTestCase(
        input=golden.input,
        actual_output=actual_output,
        expected_output=golden.expected_output
    )
    test_cases.append(test_case)

# Evaluate with metrics
evaluate(
    test_cases=test_cases,
    metrics=[relevancy_metric, faithfulness_metric]
)
```

**Option C: With Dataset**

```python
# If dataset already contains test cases
evaluate(
    test_cases=dataset.test_cases,  # or dataset itself
    metrics=[relevancy_metric, faithfulness_metric]
)
```

### Step 3: Configure Metric Parameters (Optional)

Some metrics allow configuration:

```python
# Example: Configure threshold for AnswerRelevancyMetric
relevancy_metric = AnswerRelevancyMetric(threshold=0.7)

# Metrics use LLM-as-a-judge internally
# The judge model is typically configured via environment variables
# or DeepEval's default settings (usually GPT-4)
```

### Understanding Judge Models

- **Metrics** (like `AnswerRelevancyMetric`) are the evaluation functions
- **Judge Model**: The underlying LLM used by metrics to evaluate outputs (typically GPT-4)
- Metrics internally use LLM-as-a-judge to score test cases
- You don't directly instantiate the judge model; metrics handle it internally

### Available Metric Types

- **RAG Metrics**: `AnswerRelevancyMetric`, `FaithfulnessMetric`, `ContextualRelevancyMetric`
- **Agent Metrics**: Various agent-specific metrics
- **Conversational Metrics**: `TurnRelevancyMetric`, etc.
- **Custom Metrics**: Create your own by extending `BaseMetric`

**Reference**: 
- [DeepEval Metrics Documentation](https://deepeval.com/docs/eval-metrics)
- [DeepEval End-to-End Evals Documentation](https://deepeval.com/docs/evaluation-end-to-end-llm-evals)




