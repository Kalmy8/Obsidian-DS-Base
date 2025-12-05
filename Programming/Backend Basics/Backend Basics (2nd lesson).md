**Codewords:** Synchronous, Asynchronous, Concurrency, Parallelism, `asyncio`, `multiprocessing`, `threading`, GIL.

## 1. Concurrency in Python

In the first lesson, we learned how to request data from APIs one by one (synchronously). But what if you need to make hundreds of requests? Waiting for each one to finish before starting the next would be incredibly slow.

This is where **concurrency** comes in. It's about structuring your program to handle multiple tasks at once, especially when tasks involve waiting for I/O (like network requests).

Python has several ways to achieve concurrency, each suited for different problems. We won't go into the deep details here, as we have dedicated notes for that. Instead, this lesson will serve as a high-level guide.

### Core Concepts

It is highly recommended that you study the following notes to understand the fundamentals of how Python handles concurrent operations.

-   **Deep Dive into Concurrency:** Before learning about `asyncio`, it's crucial to understand the difference between processes and threads, CPU-bound vs. I/O-bound tasks, and how the Global Interpreter Lock (GIL) affects Python programs.
    -   **➡️ [Read the detailed note: `python multiprocessing, multithreading, asyncio.md`](../../python%20multiprocessing,%20multithreading,%20asyncio.md)**

-   **Understanding `asyncio`:** `asyncio` is the modern way to handle high-concurrency I/O-bound tasks in Python. It uses a single thread with an event loop to manage thousands of connections efficiently.
    -   **➡️ [Read the detailed note: `python asyncio usage.md`](../../python%20asyncio%20usage.md)**

---

**Practice Problem: Review and Explain**

There is no coding practice for this lesson. Instead, your task is to:

1.  Read the two linked documents thoroughly.
2.  Be prepared to answer the "Key Questions" from each document.
3.  In your own words, explain to me the difference between `multiprocessing`, `threading`, and `asyncio`, and give an example of a problem where you would choose one over the others.

---

#🃏/backend-basics
**Key Questions:**

1.  According to the linked notes, what is the Global Interpreter Lock (GIL)?
?
-   The GIL is a mutex (a lock) that protects access to Python objects, preventing multiple native threads from executing Python bytecodes at the same time. This means that even on a multi-core processor, only one thread can be executing Python code at any given moment.

2.  When would you choose `multiprocessing` over `threading` or `asyncio`?
?
-   You would choose `multiprocessing` for CPU-bound tasks that can be easily parallelized (split into independent chunks). Because it uses separate processes, it is not limited by the GIL and can fully utilize multiple CPU cores.

3.  What is the main advantage of `asyncio` for a web server or a bot?
?
-   `asyncio` is extremely efficient for a high number of I/O-bound tasks. A web server or bot spends most of its time waiting for network requests and responses. `asyncio` allows a single thread to handle thousands of these connections concurrently without the overhead of creating thousands of threads. 