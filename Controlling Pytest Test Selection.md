---
type: note
status: done
tags: []
sources:
-
authors:
-
---
#pytest

This document summarizes practical ways to run **only a subset of tests** with `pytest`, plus some common conventions and best practices.
#### 1. Running tests by path (file, dir, single test)
```bash
# Run all tests in the `tests` folder
pytest tests

# Run all tests in a specific file
pytest tests/test_api_routes.py

#Run all tests in a specific directory (e.g. only e2e)
pytest tests/e2e

# Run a single test function (by node ii
pytest tests/test_mcp_routes.py::test_some_specific_case

# Run a single test method on a class
pytest tests/test_hybrid_routes.py::TestHybridRoutes::test_rest_endpoint
```
#### 2. Using `-k` expressions (by test name / keyword)

`-k` lets you select tests by **substring match** on test names and node ids, with boolean expressions:

Use `-k` for **ad‑hoc selection** when you don’t want to change code/markers.

```bash
# Run all tests containing `"hybrid"` in their name or path
pytest -k "hybrid"

# Run tests that have `"hybrid"` but not `"slow"`
pytest -k "hybrid and not slow"

# Run tests that mention `"weather"` or `"routes"`
pytest -k "weather or routes"
```

#### 3. Using markers (e.g. `slow`, `e2e`, `integration`)

##### 3.1 Registering markers in `pytest.ini`

To avoid warnings and make markers discoverable, register them in `pytest.ini` (in your repo root):

```ini
# pytest.ini
[pytest]
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    e2e: end-to-end tests
    integration: integration tests that hit multiple layers
```
##### 3.2 Defining markers in tests
You can “tag” tests with markers like `slow`, `e2e`, `integration`, etc.

```python
import pytest

@pytest.mark.slow
def test_expensive_operation():
    ...

@pytest.mark.e2e
def test_full_stack_scenario():
    ...

@pytest.mark.integration
class TestHybridRoutes:
    def test_api_and_mcp_together(self):
        ...
```
##### 3.3 Running by marker

```bash
# Run only slow tests
pytest -m slow

# Run everything except slow tests
pytest -m "not slow"

# Run only e2e tests
pytest -m e2e

# Run integration but not slow**:
pytest -m "integration and not slow"
```

#### 4. Skipping and xfail selectively

Use these when you want to control which tests effectively participate in your “green build” without deleting them.


```python
import pytest
import sys

@pytest.mark.skip(reason="temporarily disabled")
def test_old_behavior():
    ...

@pytest.mark.skipif(sys.platform == "win32", reason="Fails on Windows")
def test_non_windows_only():
    ...
```


```python
@pytest.mark.xfail(reason="Bug #123, fix pending")
def test_buggy_case():
    ...
```

## 5. Combining path, `-k`, and `-m`

You can combine selection methods:


```bash
pytest tests/e2e -m "not slow"
```


```bash
pytest tests/test_hybrid_routes.py -k "hybrid and not flaky_case_name"
```


```bash
pytest tests -m "e2e and integration" -k "weather"
```

Pytest applies **all** filters together; tests must satisfy **path AND `-k` AND `-m`**.


## 6. Speeding up feedback (subset strategies)

- **Smoke subset with markers**: mark a small set as “smoke” to run frequently:

```python
@pytest.mark.smoke
def test_critical_path():
    ...
```

```ini
[pytest]
markers =
    smoke: small, fast subset for quick feedback
```

```bash
pytest -m smoke
```

- **Run changed tests first** (with plugins like `pytest-testmon`) – optional, but can help with large suites.

- **Fail fast (flow control)**:

```bash
pytest --maxfail=1 -x
```

This doesn’t change which tests run, but stops early on failure (useful during debugging).

---

## 7. Configuring defaults in `pytest.ini`

You can encode common selection patterns or options so you don’t have to type them every time:

```ini
[pytest]
addopts = -ra -q
testpaths =
    tests
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    e2e: end-to-end tests
    integration: integration tests that hit multiple layers
    smoke: small, fast subset for quick feedback
```

Then you can just run:

```bash
pytest
```

…and rely on custom commands or CI jobs to add `-m "not slow"` or `-m e2e` as needed.

---

## 8. Recommended patterns / best practices

- **Use markers for categories**:
  - **fast vs slow**: `@pytest.mark.slow` and `-m "not slow"` for local dev.
  - **e2e / integration / unit**: clear layers for different pipelines.
  - **smoke**: small, fast subset you can run constantly.

- **Register markers in `pytest.ini`** so they’re documented and free of warnings.

- **Use path selection** (`tests/e2e`, `tests/test_*.py`) for coarse-grained slicing (e.g. “only e2e in this directory”).

- **Use `-k` for ad‑hoc runs** where you don’t want to touch code or config.

- **Keep test names descriptive**; good names make `-k` much more powerful.
