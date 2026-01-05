---
type: note
status: done
tags: []
sources:
-
authors:
-
---
# Understanding `assert_test` in DeepEval

## What is `assert_test`?

`assert_test` is DeepEval's function for evaluating LLM outputs in pytest. It:

**Key Point:** It's designed to work seamlessly with pytest, so failed evaluations become failed tests.


## Why `@observe` is Required (and When)

### **The Requirement**

When using `observed_callback` with `assert_test`, DeepEval **requires** the function to be decorated with `@observe()` from `deepeval.tracing`.

**Why?**
- DeepEval uses tracing to track function execution
- Enables component-level evaluation and observability
- Allows DeepEval to instrument the function for metrics
- Required for proper integration with DeepEval's evaluation system

**Error Without It:**
```python
# ❌ This will raise ValueError
def llm_app(input_text: str) -> str:
    return "output"

assert_test(golden=golden, observed_callback=llm_app)
# ValueError: The provided 'observed_callback' must be decorated with '@observe' from deepeval.tracing
```

### **When You DON'T Need `@observe`**

If you use the `test_case` approach (Method 2), you **don't need** `@observe` because:
- You're creating `LLMTestCase` manually
- DeepEval doesn't need to trace your function
- You have full control over test case creation

```python
# ✅ No @observe needed - using test_case directly
def llm_app(input_text: str) -> str:
    return "output"

actual_output = llm_app(golden.input)
test_case = LLMTestCase(
    input=golden.input,
    actual_output=actual_output,
    expected_output=golden.expected_output
)
assert_test(test_case=test_case, metrics=metrics)  # Works without @observe!
```

---

## Two Ways to Use `assert_test`

### **Method 1: Using `golden` + `observed_callback` (Recommended for Dev)**

**Simpler approach** - DeepEval handles test case creation automatically.

**⚠️ IMPORTANT:** The `observed_callback` function **MUST** be decorated with `@observe` from `deepeval.tracing`. This enables DeepEval's tracing system to track function execution.

```python
import pytest
from deepeval import assert_test
from deepeval.dataset import Golden, EvaluationDataset
from deepeval.tracing import observe  # Required import

# Load dataset
dataset = EvaluationDataset()
dataset.add_goldens_from_csv_file(
    file_path="./dataset.csv",
    input_col_name="input",
    expected_output_col_name="expected_output"
)

# Your LLM application function - MUST be decorated with @observe
# Option 1: No metrics (uses defaults)
@observe()  # ⚠️ REQUIRED: Without this, you'll get ValueError
def llm_app(input_text: str) -> str:
    # Your LLM logic here
    return "Generated output"

# Option 2: With metrics in @observe decorator
from deepeval.metrics import AnswerRelevancyMetric

@observe(metrics=[AnswerRelevancyMetric(threshold=0.7)])  # Metrics go HERE
def llm_app_with_metrics(input_text: str) -> str:
    return "Generated output"

# Parametrized test
@pytest.mark.parametrize("golden", dataset.goldens)
def test_llm_app(golden: Golden):
    assert_test(
        golden=golden,
        observed_callback=llm_app
        # ⚠️ DO NOT pass metrics here when using golden + observed_callback
        # metrics=[...]  # ❌ This will cause ValueError!
    )
```

**What Happens Internally:**
1. DeepEval validates that `llm_app` is decorated with `@observe` (raises `ValueError` if not)
2. `assert_test` calls `llm_app(golden.input)` to get `actual_output`
3. Creates `LLMTestCase` with:
   - `input` = `golden.input`
   - `actual_output` = result from `llm_app()`
   - `expected_output` = `golden.expected_output`
4. Evaluates using default metrics (or specified metrics)
5. Raises `AssertionError` if any metric fails

**Why `@observe` is Required:**
- Enables DeepEval's tracing system to track function execution
- Allows component-level evaluation and observability
- Required for DeepEval to properly instrument and evaluate the callback

**Advantages:**
- Cleaner code - no manual test case creation
- Automatic handling of input/output
- Less boilerplate
- Built-in tracing and observability

---

### **Method 2: Using `test_case` + `metrics` (More Control)**

**Explicit approach** - You create test cases manually.

```python
import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric
from deepeval.dataset import EvaluationDataset

# Load dataset
dataset = EvaluationDataset()
dataset.add_goldens_from_csv_file(
    file_path="./dataset.csv",
    input_col_name="input",
    expected_output_col_name="expected_output"
)

# Your LLM application function
def llm_app(input_text: str) -> tuple[str, list[str]]:
    # Your LLM logic here
    output = "Generated output"
    retrieval_context = ["context1", "context2"]
    return output, retrieval_context

# Parametrized test
@pytest.mark.parametrize("golden", dataset.goldens)
def test_llm_app(golden: Golden):
    # Call your LLM app
    actual_output, retrieval_context = llm_app(golden.input)
    
    # Create test case manually
    test_case = LLMTestCase(
        input=golden.input,
        actual_output=actual_output,
        expected_output=golden.expected_output,
        retrieval_context=retrieval_context
    )
    
    # Define metrics explicitly
    metrics = [
        AnswerRelevancyMetric(threshold=0.7),
        FaithfulnessMetric(threshold=0.8)
    ]
    
    # Assert with explicit metrics
    assert_test(
        test_case=test_case,
        metrics=metrics
    )
```

**What Happens Internally:**
1. `assert_test` receives a complete `LLMTestCase`
2. Evaluates using the specified `metrics`
3. Each metric compares `actual_output` vs `expected_output` (and `retrieval_context` if applicable)
4. Raises `AssertionError` if any metric score < threshold

**Advantages:**
- Full control over test case creation
- Can add custom fields (retrieval_context, etc.)
- Explicit metric selection
- Better for complex scenarios

---

## Complete Function Signature

```python
def assert_test(
    # Option 1: Use golden + observed_callback
    golden: Golden | None = None,
    observed_callback: Callable[[str], str] | None = None,  # MUST be decorated with @observe
    
    # Option 2: Use test_case directly
    test_case: LLMTestCase | None = None,
    
    # Metrics (optional if using golden, required if using test_case)
    metrics: list[BaseMetric] | None = None,
    
    # Optional parameters
    run_async: bool = True,  # Run metrics concurrently
    display_progress: bool = True  # Show progress bar
) -> None:
    """
    Evaluates an LLM test case using specified metrics.
    
    Raises AssertionError if any metric fails (for pytest integration).
    """
```

**Important Rules:**
- **Either** use `golden` + `observed_callback` **OR** `test_case` + `metrics`
- **⚠️ CRITICAL:** `observed_callback` **MUST** be decorated with `@observe()` from `deepeval.tracing`
  - Without `@observe`, you'll get: `ValueError: The provided 'observed_callback' must be decorated with '@observe' from deepeval.tracing`
- **⚠️ CRITICAL:** When using `golden` + `observed_callback`:
  - **DO NOT** pass `metrics` parameter to `assert_test()`
  - **DO** specify metrics in the `@observe()` decorator: `@observe(metrics=[...])`
  - If no metrics in `@observe()`, uses default metrics
- **When using `test_case` + `metrics`:**
  - Pass `metrics` as parameter to `assert_test()`
  - No `@observe` decorator needed
- `observed_callback` must be a function that takes `str` (input) and returns `str` (output)

---

## How It Works Internally (Removing the Magic)

### **Step-by-Step Process:**

**When using `golden` + `observed_callback`:**

```python
# What you write:
from deepeval.metrics import AnswerRelevancyMetric

@observe(metrics=[AnswerRelevancyMetric(threshold=0.7)])  # Metrics in decorator!
def llm_app(input_text: str) -> str:
    return "output"

assert_test(golden=golden, observed_callback=llm_app)
# ⚠️ DO NOT pass metrics parameter here!

# What DeepEval does internally (simplified):
def assert_test(golden, observed_callback, metrics=None):
    # 1. Validate that metrics are NOT passed as parameter
    if metrics is not None:
        raise ValueError(
            "You cannot provide both ('golden' + 'observed_callback') and "
            "('test_case' + 'metrics'). Choose one mode."
        )
    
    # 2. Validate @observe decorator (raises ValueError if missing)
    if not has_observe_decorator(observed_callback):
        raise ValueError(
            "The provided 'observed_callback' must be decorated with "
            "'@observe' from deepeval.tracing"
        )
    
    # 3. Extract metrics from @observe decorator
    metrics = get_metrics_from_observe_decorator(observed_callback)
    if not metrics:
        metrics = get_default_metrics()  # Usually AnswerRelevancyMetric
    
    # 4. Call your LLM app (tracing enabled via @observe)
    actual_output = observed_callback(golden.input)
    
    # 5. Create test case
    test_case = LLMTestCase(
        input=golden.input,
        actual_output=actual_output,
        expected_output=golden.expected_output
    )
    
    # 6. Evaluate each metric
    for metric in metrics:
        score = metric.measure(test_case)
        
        # 7. Check if metric passes
        if score < metric.threshold:
            raise AssertionError(
                f"Metric {metric.__class__.__name__} failed: "
                f"score {score} < threshold {metric.threshold}"
            )
    
    # 8. Log to Confident AI (if configured)
    log_to_confident_ai(test_case, metrics)
```

**When using `test_case` + `metrics`:**

```python
# What you write:
assert_test(test_case=test_case, metrics=metrics)

# What DeepEval does internally (simplified):
def assert_test(test_case, metrics):
    # 1. Validate test case has required fields
    assert test_case.input is not None
    assert test_case.actual_output is not None
    
    # 2. Evaluate each metric
    for metric in metrics:
        score = metric.measure(test_case)
        
        # 3. Check if metric passes
        if score < metric.threshold:
            raise AssertionError(
                f"Metric {metric.__class__.__name__} failed: "
                f"score {score} < threshold {metric.threshold}"
            )
    
    # 4. Log to Confident AI (if configured)
    log_to_confident_ai(test_case, metrics)
```

---

## Recommended Pattern: pytest + EvaluationDataset

### **Complete Example:**

```python
# test_llm_app.py

import pytest
from deepeval import assert_test
from deepeval.dataset import EvaluationDataset, Golden
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric
from deepeval.tracing import observe  # Required for @observe decorator

# Load dataset once (module-level)
dataset = EvaluationDataset()
dataset.add_goldens_from_csv_file(
    file_path="./evaluation_dataset.csv",
    input_col_name="query",
    expected_output_col_name="expected_answer",
    context_col_name="context"  # Optional
)

# Your LLM application - MUST be decorated with @observe
# Option 1: Metrics in @observe decorator (recommended for golden + observed_callback)
@observe(metrics=[
    AnswerRelevancyMetric(threshold=0.7, model="gpt-4o"),
    FaithfulnessMetric(threshold=0.8, model="gpt-4o")
])
def your_llm_app(query: str) -> str:
    """
    Your LLM application function.
    Takes input query, returns generated output.
    """
    # Replace with your actual LLM logic
    from openai import OpenAI
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query}]
    )
    return response.choices[0].message.content

# Parametrized test
@pytest.mark.parametrize("golden", dataset.goldens)
def test_llm_application(golden: Golden):
    """
    Test LLM application against each golden in the dataset.
    
    This test will run once for each golden, creating a separate
    test case in pytest.
    """
    assert_test(
        golden=golden,
        observed_callback=your_llm_app
        # ⚠️ DO NOT pass metrics here - they're in @observe decorator!
    )
```

### **Running the Tests:**

```bash
# Run with DeepEval CLI (recommended)
deepeval test run test_llm_app.py

# Or run with pytest directly
pytest test_llm_app.py -v
```

**What You'll See:**
```
test_llm_app.py::test_llm_application[golden-0] PASSED
test_llm_app.py::test_llm_application[golden-1] PASSED
test_llm_app.py::test_llm_application[golden-2] FAILED  # Metric failed
...
```

---

## Advanced: Custom `observed_callback` with Context

If your LLM app needs to return additional context (e.g., retrieval_context):

```python
from deepeval.test_case import LLMTestCase

def llm_app_with_context(query: str) -> tuple[str, list[str]]:
    """
    Returns (output, retrieval_context)
    """
    # Your RAG pipeline
    retrieved_chunks = retrieve(query)
    output = generate(query, retrieved_chunks)
    return output, retrieved_chunks

@pytest.mark.parametrize("golden", dataset.goldens)
def test_llm_app(golden: Golden):
    # Get output and context
    actual_output, retrieval_context = llm_app_with_context(golden.input)
    
    # Create test case with context
    test_case = LLMTestCase(
        input=golden.input,
        actual_output=actual_output,
        expected_output=golden.expected_output,
        retrieval_context=retrieval_context  # Important for RAG metrics
    )
    
    # Metrics that use retrieval_context
    metrics = [
        AnswerRelevancyMetric(threshold=0.7),
        FaithfulnessMetric(threshold=0.8),  # Needs retrieval_context
        ContextualRelevancyMetric(threshold=0.6)  # Needs retrieval_context
    ]
    
    assert_test(test_case=test_case, metrics=metrics)
```

---

## Understanding Assertion Behavior

### **What Happens When a Metric Fails?**

```python
# If AnswerRelevancyMetric scores 0.5 but threshold is 0.7:
assert_test(test_case=test_case, metrics=[AnswerRelevancyMetric(threshold=0.7)])

# Raises:
# AssertionError: Metric AnswerRelevancyMetric failed: score 0.5 < threshold 0.7
```

**In pytest:**
- Test is marked as **FAILED**
- Error message shows which metric failed and why
- Other tests continue running
- Full report available after all tests complete

### **What Happens When All Metrics Pass?**

```python
# If all metrics score above their thresholds:
assert_test(test_case=test_case, metrics=metrics)

# No exception raised
# Test is marked as PASSED
# Results logged to Confident AI (if configured)
```

---

## Common Patterns

### **Pattern 1: Simple Evaluation (Recommended for Dev)**

```python
from deepeval.tracing import observe

@observe()  # REQUIRED!
def llm_app(input_text: str) -> str:
    return "output"

@pytest.mark.parametrize("golden", dataset.goldens)
def test_llm_app(golden: Golden):
    assert_test(golden=golden, observed_callback=llm_app)
    # Uses default metrics (AnswerRelevancyMetric)
```

### **Pattern 2: Explicit Metrics with Golden + Observed Callback**

```python
from deepeval.tracing import observe

# Metrics go in @observe decorator!
@observe(metrics=[
    AnswerRelevancyMetric(threshold=0.7),
    FaithfulnessMetric(threshold=0.8)
])
def llm_app(input_text: str) -> str:
    return "output"

@pytest.mark.parametrize("golden", dataset.goldens)
def test_llm_app(golden: Golden):
    assert_test(
        golden=golden,
        observed_callback=llm_app
        # ⚠️ DO NOT pass metrics here - they're in @observe decorator!
    )
```

**Alternative: Use test_case + metrics if you want to pass metrics as parameter:**

```python
# No @observe needed when using test_case
def llm_app(input_text: str) -> str:
    return "output"

@pytest.mark.parametrize("golden", dataset.goldens)
def test_llm_app(golden: Golden):
    actual_output = llm_app(golden.input)
    test_case = LLMTestCase(
        input=golden.input,
        actual_output=actual_output,
        expected_output=golden.expected_output
    )
    metrics = [
        AnswerRelevancyMetric(threshold=0.7),
        FaithfulnessMetric(threshold=0.8)
    ]
    assert_test(
        test_case=test_case,
        metrics=metrics  # ✅ Metrics as parameter when using test_case
    )
```

### **Pattern 3: Full Control**

```python
@pytest.mark.parametrize("golden", dataset.goldens)
def test_llm_app(golden: Golden):
    actual_output, context = llm_app(golden.input)
    test_case = LLMTestCase(
        input=golden.input,
        actual_output=actual_output,
        expected_output=golden.expected_output,
        retrieval_context=context
    )
    assert_test(test_case=test_case, metrics=metrics)
```

---

## Key Takeaways

1. **`assert_test` is pytest-friendly**: Raises `AssertionError` on failure
2. **Two main approaches** (mutually exclusive):
   - **Mode 1:** `golden` + `observed_callback` - **⚠️ REQUIRES `@observe` decorator**
     - Metrics go in `@observe(metrics=[...])` decorator
     - **DO NOT** pass `metrics` parameter to `assert_test()`
   - **Mode 2:** `test_case` + `metrics` - **No `@observe` needed**
     - Metrics passed as parameter: `assert_test(test_case=..., metrics=[...])`
3. **`@observe` is mandatory** when using `observed_callback`:
   - Enables DeepEval's tracing system
   - Required for component-level evaluation
   - Without it: `ValueError: The provided 'observed_callback' must be decorated with '@observe'`
4. **Metrics location depends on mode**:
   - Mode 1: `@observe(metrics=[...])` decorator
   - Mode 2: `metrics=[...]` parameter to `assert_test()`
5. **Metrics are evaluated**: Each metric compares actual vs expected
6. **Threshold determines pass/fail**: Score must be >= threshold
7. **Works with parametrization**: One test per golden in dataset
8. **Results are logged**: To Confident AI if configured

---

## Troubleshooting

### **Issue: "You cannot provide both ('golden' + 'observed_callback') and ('test_case' + 'metrics')"**

**Error Message:**
```
ValueError: You cannot provide both ('golden' + 'observed_callback') and ('test_case' + 'metrics'). Choose one mode.
```

**Cause:** You're trying to pass `metrics` parameter to `assert_test()` when using `golden` + `observed_callback` mode.

**Solution:**

**Option 1: Put metrics in `@observe` decorator (Recommended)**
```python
from deepeval.tracing import observe
from deepeval.metrics import GEval

correctness_metric = GEval(
    name="Correctness",
    criteria="Evaluate correctness"
)

@observe(metrics=[correctness_metric])  # ✅ Metrics go HERE
def llm_app(input_text: str) -> str:
    return "output"

@pytest.mark.parametrize("golden", dataset.goldens)
def test_llm_app(golden: Golden):
    assert_test(
        golden=golden,
        observed_callback=llm_app
        # ✅ DO NOT pass metrics parameter here
    )
```

**Option 2: Use test_case + metrics instead**
```python
# No @observe needed
def llm_app(input_text: str) -> str:
    return "output"

@pytest.mark.parametrize("golden", dataset.goldens)
def test_llm_app(golden: Golden, correctness_metric: GEval):
    actual_output = llm_app(golden.input)
    test_case = LLMTestCase(
        input=golden.input,
        actual_output=actual_output,
        expected_output=golden.expected_output
    )
    assert_test(
        test_case=test_case,  # ✅ Use test_case instead
        metrics=[correctness_metric]  # ✅ Now metrics parameter works
    )
```

### **Issue: "The provided 'observed_callback' must be decorated with '@observe' from deepeval.tracing"**

**Error Message:**
```
ValueError: The provided 'observed_callback' must be decorated with '@observe' from deepeval.tracing
```

**Cause:** Your `observed_callback` function is missing the `@observe()` decorator.

**Solution:**
```python
# ❌ Wrong - Missing @observe decorator
def llm_app(input_text: str) -> str:
    return "output"

assert_test(golden=golden, observed_callback=llm_app)  # Raises ValueError

# ✅ Correct - With @observe decorator
from deepeval.tracing import observe

@observe()  # REQUIRED!
def llm_app(input_text: str) -> str:
    return "output"

assert_test(golden=golden, observed_callback=llm_app)  # Works!
```

**Alternative:** Use `test_case` approach instead (no `@observe` needed):
```python
# ✅ Alternative - No @observe needed
def llm_app(input_text: str) -> str:
    return "output"

actual_output = llm_app(golden.input)
test_case = LLMTestCase(
    input=golden.input,
    actual_output=actual_output,
    expected_output=golden.expected_output
)
assert_test(test_case=test_case, metrics=metrics)
```

### **Issue: "observed_callback must be callable"**

```python
# ❌ Wrong
assert_test(golden=golden, observed_callback=llm_app())  # Called function

# ✅ Correct
assert_test(golden=golden, observed_callback=llm_app)  # Function reference
```

### **Issue: "test_case must have input and actual_output"**

```python
# ❌ Wrong
test_case = LLMTestCase(input="query")  # Missing actual_output

# ✅ Correct
test_case = LLMTestCase(
    input="query",
    actual_output="answer"
)
```

### **Issue: "No metrics provided"**

```python
# ❌ Wrong (when using test_case)
assert_test(test_case=test_case)  # No metrics

# ✅ Correct
assert_test(test_case=test_case, metrics=[AnswerRelevancyMetric()])
```

---

## References

- [DeepEval Unit Testing in CI/CD](https://deepeval.com/docs/evaluation-unit-testing-in-ci-cd)
- [DeepEval End-to-End Evals](https://deepeval.com/docs/evaluation-end-to-end-llm-evals)
- [DeepEval Datasets](https://deepeval.com/docs/evaluation-datasets)

