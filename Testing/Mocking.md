
- Mocking means creating objects that mimic the behavior of real objects
- Use-cases for mocking include:
	- External systems: DB, API connections etc.
	- Some components, dependencies of our own system which requires remote connection
	- Some undetermenistic components, which might produce different results during a program run (e.g. random module)
- **There are 2 main types of Mocks:**

### 1.  Patches

#### Replace a function's return value

- Useful for simulating error conditions 
- **Precision:** usually we want to patch only remote calls themselves to keep our tests as close to the real world as possible
	- Patching the whole method: ![[Pasted image 20251206000431.png | 500]]
	- Patching only the remote call![[Pasted image 20251206000547.png | 500]]

#### Replace a whole function (side-effect)

- **When to use?**
	- When the function has **complex side-effects** that you don't want to execute in tests (writing files, triggering emails, sleeping, heavy CPU, etc.)
	- When you want to replace a function with a **simple stub** that always succeeds (e.g. `send_email` → `lambda *a, **kw: None`)
	- When the original function is **non-deterministic** (uses `random`, `time`, real network, etc.) and you want a stable behavior
- ![[Pasted image 20251206001110.png]]

### 2. Mocks

- Allow to fully control the whole object's behavior: methods, attributes
- **There are 3 main types of mocks:**
	- `Mock` - allows you to create a Mock
	-  `MagicMock` does the same + implements all the python's "magic" methods like `__repr__`, `__getitem__` etc.
	- `AsyncMock` - same as `Mock`, but for **async functions** (`async def`). It can be `await`-ed and records calls to `await some_async_mock()`.
- Demonstration on Mock object behavior: ![[Pasted image 20251206001433.png | 500]]
- We use **`spec` parameter** to narrow down the possibilities of our Mock object: ![[Pasted image 20251206002707.png]]
- Demonstration on Mock + Patch techniques combination in a real scenario: ![[Pasted image 20251206001701.png | 600]]
	- Here, we have used patching to make the `requests.get()` call return a `Mock Response`, while we control the exact content of that `Response object`

- **Mock allow for tracking calls and provide statistics:**
	- `mock.called` – `True`/`False`, was it ever called?
	- `mock.call_count` – how many times was it called
	- `mock.call_args` – arguments from the **last** call
	- `mock.call_args_list` – list of all calls with their args
	- `mock.reset_mock()` – clear all call history
	- Assertion helpers:
		- `mock.assert_not_called()`
		- `mock.assert_called()`
		- `mock.assert_called_once()`
		- `mock.assert_called_with(*args, **kwargs)`
		- `mock.assert_called_once_with(*args, **kwargs)`	
- Mocks can be used to mimic methods using **`return_value`** – always gives back the same value (while still tracking the mock calls):
  ```python
	  get_status: Mock = Mock()
	  get_status.return_value = {"status": "ok"}
	```
- As well as patches, Mocks do offer `side_effect` parameter:
	- can be a **callable**: `side_effect=fn` → mock will call `fn(*args, **kwargs)` and return its result:
	  ```python
	  def add(x: int, y: int) -> int:
        print(f"  add called with x={x}, y={y}")
        return x + y

    adder: Mock = Mock(side_effect=add)

    print("demo_side_effect_callable:", adder(2, 3))  
    # 5
    print("demo_side_effect_callable:", adder(10, -1))
    # 9  
	  ```
	- Simcan be a **list/tuple**: `side_effect=[1, 2, 3]` → each call returns next value, then raises `StopIteration`:
	  ```python
	  next_id: Mock = Mock(side_effect=[100, 101, 102])

    print("demo_side_effect_sequence:", next_id())  # 100
    print("demo_side_effect_sequence:", next_id())  # 101
    print("demo_side_effect_sequence:", next_id())  # 102
	  ```
	- **Simulate Exceptions on remote calls:** `side_effect=ValueError("boom")` → mock raises this exception when called:
```python
	   # This mock ALWAYS raises when called
    failing_call: Mock = Mock(side_effect=RuntimeError("network down"))

    try:
        failing_call()
    except RuntimeError as exc:
        print("demo_side_effect_exception: raised", repr(exc))
	  ```