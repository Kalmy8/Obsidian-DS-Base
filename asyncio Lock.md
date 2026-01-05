---
type: note
status: done
tags: [tech/python]
sources:
-
authors:
-
---

`asyncio.Lock()` is a synchronization primitive used to prevent **race conditions** when multiple async tasks try to access or modify a shared resource simultaneously.

Here is a breakdown of **Where**, **Why**, and **When** to use it, referenced against your codebase.

### 1. WHERE to use it
You typically initialize a lock in your class `__init__` and use it with the `async with` context manager around a "critical section" of code.

**Example from your codebase:**
In `agent-swarms-poc/marketplace/src/marketplace/in_memory_agent_repository.py`:

```python:agent-swarms-poc/marketplace/src/marketplace/in_memory_agent_repository.py
// ... existing code ...
 def __init__(self):
 """Initialize in-memory repository."""
 self._agents: dict[str, AgentProfile] = {}
 self._lock = asyncio.Lock() # 1. Initialize the lock

 async def create_agent(self, profile: AgentProfile) -> None:
 # ... 
 async with self._lock: # 2. Acquire lock before accessing shared state
 # Check for duplicate base_url
 for existing_agent in self._agents.values():
 if existing_agent.base_url == profile.base_url:
// ... existing code ...
 # Create new agent
 self._agents[profile.agent_id] = profile
```

### 2. WHY use it
In `asyncio`, although your code runs on a single thread, execution can be interrupted and switched to another task whenever you reach an `await` statement.

If you have a multi-step operation (Read → Check → Write) and you `await` somewhere in the middle, another task could change the data while the first task is paused.

* **Without Lock**: Task A reads "User count is 10". Task A yields (waits). Task B reads "User count is 10". Task A resumes and writes "11". Task B resumes and writes "11". **Result: 11 (Should be 12).**
* **With Lock**: Task A acquires lock. Task A reads "10". Task A yields. Task B tries to acquire lock -> **Waits**. Task A writes "11" and releases lock. Task B acquires lock, reads "11", writes "12".

**Note on your specific code:**
In your `InMemoryAgentRepository`, there are actually *no* `await` calls inside the `async with self._lock:` block. Because `asyncio` is single-threaded cooperatively, this specific block is naturally atomic even without the lock (execution cannot switch without an `await`). However, keeping the lock is **good practice** because:
1. It future-proofs the code: if you later change the in-memory check to a DB call (`await db.check_user()`), the lock becomes critical.
2. It communicates intent: "This block modifies shared state and must be atomic."

### 3. WHEN to use it
Use `asyncio.Lock()` when **ALL** of the following are true:
1. **Shared State**: You have a variable (like `self._agents` or a file) accessed by multiple concurrent tasks.
2. **Mutation**: At least one task writes/modifies that state.
3. **Concurrency Points**: The operation involves multiple steps with `await` points (or you want to be safe against future changes adding them).

**Common Scenarios:**
* **Preventing Double-Submit**: Checking if a user exists before creating them (like in your `create_agent`).
* **Rate Limiting**: Ensuring only N tasks access an API endpoint at once.
* **File I/O**: Ensuring one task finishes writing to a file before another starts.

### Summary
| Component | Description |
| :----------------- | :--------------------------------------------------------------------------------------------------- |
| **Initialization** | `self.lock = asyncio.Lock()` in `__init__` |
| **Usage** | `async with self.lock:` around the critical code block. |
| **Purpose** | Ensures that block of code is executed by only one Task at a time, protecting shared data integrity. |