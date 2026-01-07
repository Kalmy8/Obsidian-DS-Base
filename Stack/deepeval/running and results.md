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
# Running DeepEval & Observing Results

## Core Commands

### **Running Tests**

The primary command for running evaluations:

```bash
deepeval test run <test_file.py>
```

**Examples:**
```bash
# Run a single test file
deepeval test run tests/eval/test_quality.py

# Run all tests in a directory
deepeval test run tests/

# Run with pytest directly (alternative)
pytest tests/eval/test_quality.py -v
```

**Note:** Use `deepeval test run` instead of plain `pytest` to get:


## Important Flags

### **Parallelization (`-n` / `--num-workers`)**

Run test cases concurrently for faster execution.

```bash
deepeval test run test_file.py -n 4
```

**Use Cases:**
- Large datasets (100+ test cases)
- Slow metrics (LLM-as-a-judge)
- CI/CD pipelines where speed matters

**Recommendations:**
- Start with `-n 2` or `-n 4`
- Monitor API rate limits
- Don't exceed provider rate limits

---

### **Cache (`-c` / `--cache`)**

Use cached results to avoid re-evaluating unchanged test cases.

```bash
deepeval test run test_file.py -c
```

**How It Works:**
- DeepEval caches metric results based on input/output hash
- If input/output unchanged, uses cached score
- Saves time and API costs

**When to Use:**
- Re-running same tests
- Iterative development
- Cost optimization

**Cache Location:**
- Stored locally in `.deepeval/` directory
- Automatically invalidated when inputs change

---

### **Ignore Errors (`-i` / `--ignore-errors`)**

Continue test run even if some metrics encounter errors.

```bash
deepeval test run test_file.py -i
```

**Use Cases:**
- Large test suites where some failures are expected
- Network issues causing intermittent failures
- Testing with unstable metrics

**Behavior:**
- Failed metrics are logged but don't stop execution
- Final report shows all errors
- Useful for debugging multiple issues

---

### **Verbose Mode (`-v` / `--verbose`)**

Display detailed output during evaluation.

```bash
deepeval test run test_file.py -v
```

**What You'll See:**
- Detailed metric calculations
- Step-by-step evaluation process
- Intermediate scores and reasoning
- API calls and responses (if enabled)

**Use Cases:**
- Debugging metric failures
- Understanding evaluation logic
- Development and testing

---

### **Skip Test Cases (`-s` / `--skip`)**

Skip test cases with missing or insufficient parameters.

```bash
deepeval test run test_file.py -s
```

**When Test Cases Are Skipped:**
- Missing `actual_output`
- Missing `expected_output` (for certain metrics)
- Missing `retrieval_context` (for RAG metrics)
- Invalid test case structure

**Use Cases:**
- Partial datasets
- Incremental test case creation
- Testing with incomplete data

---

### **Identifier (`-id` / `--identifier`)**

Assign a custom name to the test run.

```bash
deepeval test run test_file.py -id "Production Evaluation v2.1"
```

**Benefits:**
- Easier identification in Confident AI
- Better organization of test runs
- Useful for CI/CD pipelines

**Best Practices:**
- Use descriptive names
- Include version numbers
- Include date/timestamp in CI/CD

---

### **Display Mode (`-d` / `--display-mode`)**

Control which test cases are displayed in terminal output.

```bash
# Show only failing tests
deepeval test run test_file.py -d failing

# Show only passing tests
deepeval test run test_file.py -d passing

# Show all tests (default)
deepeval test run test_file.py -d all
```

**Use Cases:**
- `failing`: Focus on issues during debugging
- `passing`: Verify successful tests
- `all`: Complete overview

---

### **Repeats (`-r` / `--repeats`)**

Repeat each test case multiple times.

```bash
deepeval test run test_file.py -r 3
```

**Use Cases:**
- Testing consistency/stability
- Averaging scores across runs
- Handling non-deterministic outputs

**Note:** Each repeat is evaluated separately and logged.

---

## Combining Flags

You can combine multiple flags for powerful test runs:

```bash
# Fast, cached, verbose run with custom name
deepeval test run test_file.py -n 4 -c -v -id "Quick Check
# Ignore errors, show only failures, skip invalid cases
deepeval test run test_file.py -i -d failing -s

# Parallel, cached, repeat for stability testing
deepeval test run test_file.py -n 2 -c -r 3
```

---

## Configuration Commands

### **Login to Confident AI**

Authenticate to enable cloud features and result viewing.

```bash
deepeval login
```

**What It Does:**
- Opens browser for authentication
- Stores credentials locally
- Enables result syncing to Confident AI

**Benefits:**
- View results in web dashboard
- Share test reports
- Track trends over time
- Team collaboration

---

### **View Latest Results**

Open the latest test run in your browser.

```bash
deepeval view
```

**What You'll See:**
- Detailed test run report
- Metric scores and reasons
- Pass/fail status
- Trends and comparisons
- Traces (if using tracing)

---

### **Logout**

Sign out from Confident AI.

```bash
deepeval logout
```

---

### **Model Configuration**

Set default models for evaluations:

```bash
# Set OpenAI model
deepeval set-openai --model=gpt-4.1 --save

# Set Anthropic model (via env var)
export ANTHROPIC_API_KEY=your-key

# Set Gemini model
deepeval set-gemini --model-name=gemini-2.0-flash-001 --google-api-key=key --save

# Unset a model
deepeval unset-openai
```

**The `--save` Flag:**
- Persists configuration across sessions
- Saves to `.deepeval/config.json`
- Recommended for consistent evaluations

---

## Result Observation

### **Terminal Output**

After running tests, DeepEval displays:

```
Running tests...
[1/10] Test Case 1: PASSED
  AnswerRelevancyMetric: 0.85 (threshold: 0.7)
  Reason: The output is highly relevant to the input query.

[2/10] Test Case 2: FAILED
  AnswerRelevancyMetric: 0.65 (threshold: 0.7)
  Reason: The output is partially relevant but misses key details.

...

Summary:
- Total: 10
- Passed: 8
- Failed: 2
- Success Rate: 80%
```

**Key Information:**
- Test case status (PASSED/FAILED)
- Metric scores vs thresholds
- Reasons for scores
- Summary statistics

---

### **Confident AI Dashboard**

After logging in and running tests:

**Access:**
```bash
deepeval view
```

**Features:**
- **Test Run Overview**: Summary of all test runs
- **Detailed Metrics**: Scores, reasons, trends
- **Comparison**: Compare different test runs
- **Traces**: View execution traces (if using tracing)
- **Filtering**: Filter by date, status, metrics
- **Export**: Download results as CSV/JSON

**Dashboard Sections:**
1. **Overview**: High-level statistics
2. **Test Cases**: Individual test case details
3. **Metrics**: Metric performance breakdown
4. **Trends**: Performance over time
5. **Traces**: Execution traces (if enabled)

---

### **Programmatic Access**

Access results programmatically:

```python
from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

metric = AnswerRelevancyMetric(threshold=0.7)
test_case = LLMTestCase(
    input="What is Python?",
    actual_output="Python is a programming language."
)

# Evaluate
evaluate(test_cases=[test_case], metrics=[metric])

# Access results
print(f"Score: {metric.score}")
print(f"Reason: {metric.reason}")
print(f"Success: {metric.success}")
```

**Available Properties:**
- `metric.score`: Numeric score (0.0-1.0)
- `metric.reason`: Explanation of the score
- `metric.success`: Boolean pass/fail
- `metric.threshold`: Threshold value

---

## Understanding Results

### **Score Interpretation**

**Score Range:** 0.0 to 1.0
- **0.0-0.3**: Poor performance
- **0.4-0.6**: Moderate performance
- **0.7-0.9**: Good performance
- **0.9-1.0**: Excellent performance

**Pass/Fail:**
- **PASS**: `score >= threshold`
- **FAIL**: `score < threshold`

### **Common Result Patterns**

**All Tests Passing:**
```
Summary:
- Total: 10
- Passed: 10
- Failed: 0
- Success Rate: 100%
```
✅ Model meets quality standards

**Some Tests Failing:**
```
Summary:
- Total: 10
- Passed: 7
- Failed: 3
- Success Rate: 70%
```
⚠️ Review failing test cases, adjust thresholds, or improve model

**All Tests Failing:**
```
Summary:
- Total: 10
- Passed: 0
- Failed: 10
- Success Rate: 0%
```
❌ Critical issues - check:
- Model configuration
- Input/output format
- Metric thresholds
- Test case validity

---

## Environment Variables

### **API Keys**

```bash
# OpenAI
export OPENAI_API_KEY=your-key

# Anthropic
export ANTHROPIC_API_KEY=your-key

# Google (Gemini)
export GOOGLE_API_KEY=your-key

# AWS (Bedrock)
export AWS_ACCESS_KEY_ID=your-key
export AWS_SECRET_ACCESS_KEY=your-key
export AWS_REGION=us-east-1
```

### **DeepEval Configuration**

```bash
# Confident AI API Key (optional, for cloud features)
export CONFIDENT_API_KEY=your-key

# Disable telemetry
export DEEPEVAL_DISABLE_TELEMETRY=true

# Custom cache directory
export DEEPEVAL_CACHE_DIR=/custom/path
```

### **Using .env File**

Create `.env` file in project root:

```bash
OPENAI_API_KEY=your-key
ANTHROPIC_API_KEY=your-key
CONFIDENT_API_KEY=your-key
```

DeepEval automatically loads `.env` files.

---

## Common Workflows

### **Development Workflow**

```bash
# 1. Run tests with verbose output
deepeval test run tests/ -v

# 2. View results
deepeval view

# 3. Fix issues and re-run
deepeval test run tests/ -c  # Use cache for unchanged tests
```

### **CI/CD Workflow**

```bash
# Run with parallelization and custom identifier
deepeval test run tests/ \
    -n 4 \
    -id "CI Run $(date +%Y%m%d-%H%M%S)" \
    -d failing \
    -i  # Ignore errors to get full report
```

### **Production Evaluation**

```bash
# Comprehensive evaluation
deepeval test run tests/ \
    -n 8 \
    -c \
    -id "Production Eval v2.1" \
    -r 3  # Repeat for stability
```

### **Debugging Workflow**

```bash
# Verbose, show only failures, ignore errors
deepeval test run tests/ \
    -v \
    -d failing \
    -i \
    -s  # Skip invalid test cases
```

---

## Troubleshooting

### **Issue: "No API key found"**

**Solution:**
```bash
# Set environment variable
export OPENAI_API_KEY=your-key

# Or use .env file
echo "OPENAI_API_KEY=your-key" > .env
```

### **Issue: Tests running slowly**

**Solutions:**
```bash
# Use parallelization
deepeval test run tests/ -n 4

# Use caching
deepeval test run tests/ -c

# Use cheaper/faster models
deepeval set-openai --model=gpt-3.5-turbo
```

### **Issue: Rate limit errors**

**Solutions:**
```bash
# Reduce parallelization
deepeval test run tests/ -n 2  # Instead of -n 8

# Use caching
deepeval test run tests/ -c

# Add delays between requests (if supported)
```

### **Issue: Can't view results in browser**

**Solutions:**
```bash
# Ensure you're logged in
deepeval login

# Check if test run completed successfully
deepeval view

# Verify Confident AI connection
deepeval logout && deepeval login
```

---

## Best Practices

1. **Use Descriptive Identifiers**: Include version numbers, dates, or feature names
2. **Enable Caching**: Use `-c` flag to save time and costs
3. **Parallelize Wisely**: Start with `-n 2` or `-n 4`, monitor rate limits
4. **Review Failing Tests**: Use `-d failing` to focus on issues
5. **Track Trends**: Use Confident AI to monitor performance over time
6. **Set Reasonable Thresholds**: Don't set thresholds too high initially
7. **Use Verbose Mode**: When debugging, use `-v` for detailed output
8. **Save Configurations**: Use `--save` flag for model configurations

---

## References

- [DeepEval CLI Documentation](https://deepeval.com/docs/command-line-interface)
- [Flags and Configs](https://deepeval.com/docs/evaluation-flags-and-configs)
- [Confident AI Dashboard](https://deepeval.com/docs/confident-ai)


ё