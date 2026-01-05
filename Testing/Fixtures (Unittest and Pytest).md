---
type: note
status: done
tags:
- tech/stack/pytest
- tech/testing
sources:
- '[[Test and Behavior Driven Development Course]]'
authors:
- null
---
### Main Idea

- are used to set up **an initial state of the system before the test run**
	- for example, placing some data in the database
	- set up/create fake objects (mocks)
- **fixtures provide an initial state for the each test independently**
	- This means that if one of your tests delete some record from the database - the other test won't notice that (cause all the tests run in isolation with respect to fixtures)

### Unittest
- **Unittest** provides 6 standard fixtures as **hooks** (methods you override):![[Pasted image 20251205231606.png]]
	- They can be combined: If your test module contains all 3 methods, that means that unittest will:
		- first execute setUpModule once, 
		- then setUpClass for each class, 
		- then setUp for each test...
		- then tearDown for each test
		- then tearDown for each class
		- then tearDownModule once

This is the core building block of tests in pytest. It is a way to create reusable setup code.

### Pytest

- Pytest uses a completely different approach called **Dependency Injection**. It does not limit you to 6 specific methods.
- **The Core Difference:**
	- **Unittest**: You **override** standard methods (`setUp`, `tearDown`). You access data via `self`
	- **Pytest**: You **request** fixtures by naming them as arguments. `pytest` finds them, executes them, and passes the return value.
- Pytest replaces the fixed hierarchy with flexible **Scopes**:

| Unittest Hook | Pytest Equivalent |
| :---------------- | :---------------------------------------------------------- |
---
| `setUp` | `@pytest.fixture` |
| `setUpClass` | `@pytest.fixture(scope="class")`<br> |
| `setUpModule` | `@pytest.fixture(scope="module")` |
| *(No equivalent)* | `@pytest.fixture(scope="session")`<br>(once per entire run) |
- **SetUp and TearDown difference:**
	- In `unittest`, setup and teardown are separate methods. In `pytest`, they are often in the **same function** using `yield`:

```python
import pytest

@pytest.fixture
def database_connection():
 # SETUP: Everything before yield
 conn = connect_to_db()
 
 yield conn # The test runs here!
 
 # TEARDOWN: Everything after yield
 conn.disconnect()
```
- **Composability:** Fixtures can use other fixtures:
```python
import pytest

@pytest.fixture
def mock_buyer_sdk():
	...

# This fixture request mock_buyer_sdk fixture before it runs 
@pytest.fixture
def buyer_example(mock_buyer_sdk, ...):
 # SETUP: Everything before yield
 conn = mock_buyer_sdk.establish_connection()
 
 yield conn # The test runs here!
 
 # TEARDOWN: Everything after yield
 conn.disconnect()
```
