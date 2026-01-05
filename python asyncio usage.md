---
type: note
status: done
tags: ['tech/python']
sources:
-
authors:
-
---

#🃏/job-interview #🃏/semantic/python

[Асинхронный python без головной боли](https://habr.com/ru/articles/667630/)

## Theory: Understanding Asynchronous Python

### Synchronous vs. Asynchronous: A Breakfast Analogy

To understand `asyncio`, we first need to grasp the difference between synchronous and asynchronous execution.

Imagine you're making breakfast:

- **Synchronous (one-by-one):** You put bread in the toaster and wait 2 minutes for it to finish. Only after the toast is ready, you start brewing coffee and wait another 3 minutes. The total time is 5 minutes. During the waiting periods, you are idle and not doing any work. This is **synchronous** programming—tasks are executed one after another.

- **Asynchronous (multi-tasking):** You start the coffee maker (a 3-minute task). While it's brewing, you don't just stand there; you immediately put bread in the toaster (a 2-minute task). You can manage both jobs within the same period. The total time is only 3 minutes (the length of the longest task). This is **asynchronous** programming.

In programming, many tasks are "I/O-bound" (Input/Output bound), like waiting for a response from a website, a database, or a file on the disk. With synchronous code, your entire program freezes while waiting for these operations. Asynchronous code allows your program to switch to other useful work while it waits, making it dramatically more efficient for I/O-heavy applications like web servers, bots, and API clients.

### How `asyncio` Works: Coroutines and the Event Loop

`asyncio` is Python's framework for writing asynchronous code. It manages tasks using two key components:

1. **Coroutines (Co-operative Functions):** These are special functions you define with `async def`. When you call one, it doesn't run immediately. Instead, it returns a "coroutine object"—a package of work that *can* be run. Coroutines are "co-operative" because they are designed to pause themselves at specific points to let other tasks run.

2. **The Event Loop:** This is the core of `asyncio`. It acts as a scheduler or a manager. It keeps track of all the tasks (coroutines) and decides which one to run at any given time. When a running task pauses itself, the event loop looks for another task that is ready to run and switches to it.

Think of the event loop as a chef in a kitchen with only one stove burner (a single CPU thread). The chef has multiple pots (coroutines) on the counter. The chef puts one pot on the burner. If that pot just needs to simmer for a while (an I/O wait), the chef takes it off the burner and puts another pot on. The chef keeps switching between the pots, ensuring that the single burner is always doing useful work. This way, all the food gets cooked efficiently without the chef just waiting around.

### `async` and `await`: The Keywords of Co-operation

The `async` and `await` keywords are the syntax that makes this co-operation possible.

- `async def` creates a coroutine function. It's a label that tells Python, "This function can be paused and resumed."
- `await` is the pause button. You use it inside a coroutine to call another coroutine (usually one that performs an I/O operation). It effectively tells the event loop: "I'm about to wait for this result. You can pause me and go run some other tasks. Come back to me when the result is ready."

The most important concept to remember is that **`await` yields control back to the event loop.**

Let's see a step-by-step example:

```python
import asyncio
import time

async def make_coffee():
---
 print("Starting to make coffee")
 # await pauses this function and lets the event loop run other tasks
 await asyncio.sleep(3) # Simulate a 3-second I/O wait (e.g., brewing)
 print("Finished making coffee")
 return "Coffee"

async def toast_bread():
 print("Starting to toast bread")
 # await pauses this function
 await asyncio.sleep(2) # Simulate a 2-second I/O wait
 print("Finished toasting bread")
 return "Toast"

async def main():
 start_time = time.time()
 
 # asyncio.gather runs the coroutines concurrently.
 # It waits for all of them to finish and returns the results.
 print("Starting breakfast preparation...")
 results = await asyncio.gather(
 make_coffee(),
 toast_bread()
 )
 
 end_time = time.time()
 print(f"Breakfast is ready: {results[0]} and {results[1]}")
 print(f"Total time: {end_time - start_time:.2f} seconds")

# asyncio.run() starts the event loop and runs the main() coroutine
asyncio.run(main())
```

**Execution Flow:**
1. `asyncio.run(main())` starts the event loop.
2. The event loop starts running `main()`.
3. `main()` calls `asyncio.gather()` with the two coroutines (`make_coffee` and `toast_bread`). `gather` tells the event loop to run both.
4. The event loop might start `make_coffee()` first. It prints "Starting to make coffee" and then hits `await asyncio.sleep(3)`. `make_coffee()` is paused, and control goes back to the event loop.
5. The event loop sees `toast_bread()` is ready to run. It starts it. It prints "Starting to toast bread" and hits `await asyncio.sleep(2)`. `toast_bread()` is also paused.
6. Now, the event loop waits. After 2 seconds, the `sleep` in `toast_bread()` is over. The event loop resumes `toast_bread()`. It prints "Finished toasting bread" and returns.
7. After another 1 second (total 3 seconds), the `sleep` in `make_coffee()` is over. The event loop resumes `make_coffee()`. It prints "Finished making coffee" and returns.
8. Now that both tasks given to `gather` are complete, `gather` returns the results to `main()`.
9. `main()` prints the final messages. The whole process took about 3 seconds, not 5!

## Key questions
Provide a simple asyncio example which will run multiple functions asynchronously and will gather the returned values of that functions
?
```python
import asyncio 
 
async def busy1()->str: 
 print('Busy1 starts working...') 
 await asyncio.sleep(2) 
 print('Busy1 ends working...') 
 return 'result1' 
 
async def busy2()->str: 
 print('Busy2 starts working...') 
 await asyncio.sleep(2) 
 print('Busy2 ends working...') 
 return 'result2' 
 
async def main(): 
 results = await asyncio.gather(busy1(), busy2()) 
 print(results) 
 
asyncio.run(main())
```
<!--SR:!2026-02-03,255,330-->
