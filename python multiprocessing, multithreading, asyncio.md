
What is a process? What is a thread?
?
- Process - a launched program, which do operates some allocated resources, such as memory and computation time.
- Every process has one or more threads (threads are also called lightweight processes). These threads share resources with each other but operate independently.
<!--SR:!2025-02-23,64,310-->

### CPU and I/O - bounded tasks
This terminology will be used later in the note, so let's clarify what does it mean:

What are the CPU and I/O-bounded tasks? How to execute these tasks efficiently/faster?
?
- CPU-bounded tasks are heavy computational tasks which take a lot of processing time to be executed.
	- If we have to complete such a task faster, **we recruit more computational power** by using distributed computing frameworks like Dask, Spark, or multiprocessing parallel computations.
- I/O tasks are tasks related from input/output of some data, for example tasks like reading/writing from a web-server, from a remote database, from a user and etc. This tasks themselves are not expensive, but have to wait for some data exchange to run off. Some of such tasks may run infinitely (accepting new users connections on a web-server).
	- With such tasks, we should make sure that awaiting for new data exchange does not suspect the whole application, so we use concurrency/asynchronous execution.
<!--SR:!2025-02-22,63,310-->

### Physical, logical cores
Every modern CPU has at least **multiple physical cores** and, some of them, also have **multiple logical cores** (hyperthreading from Intel).

What are the physical and the logical CPU cores? 
- Physical cores are the CPU areas with their own independent computational power and L1-cache memory, although they do share other memory with each other.
- Logical cores are abstract, virtual non-real cores. It's a technology which splits one physical core into multiple logical-independent areas, which can efficiently run multiple threads while smart-sharing the physical core resources in between.

Both logical and physical cores can be used to execute multiple processes and threads. **There are 3 possible states** of how the switching between them can be done:

#### Parallel running (No switching)
Parallel running involves **using multiple physical cores**, which increases the total computational resources available.

> [!quote] Note:
> **Parallel running is the only way to deal well with some heavy CPU-bonded tasks** because the amount of computational power is increased by the amount of recruited physical cores.


#### Concurrent running (SMT)
This is the situation when \<N> threads take advantage of \<N> (the actual number for most of the modern processors equals to 2) logical cores to **smart-share resources of one physical core**.

When threads run concurrently, they take turns using the core’s execution resources, while:
- Both threads stay resident on the core at the same time. They do share resources, but they don’t get completely swapped out.
- Switching between the threads is hardware-level and happens extremely quickly (within a single clock cycle).
- If one thread stalls (e.g., waiting for memory), the other thread continues execution with minimal delay and utilizes the idle resources.

> [!quote] Note:
> **Concurrent running is not benefitial, if both threads are dealing with some heavy CPU-bonded tasks** (which require a lot of extensive calculation), because the amount of work you have to does not become less because of the concurrent execution.
> 
> In fact, the concurrent execution here will be even slower, because you will loose some time switching in-between the processes.
> 
> On the other hand,**it is benefitial, if at least one of the threads executes some I/O-bonded task**. When such task becomes idle and awaits for some input (like web-socket, or user input, or DB connection...), the other process will take the spare resources quickly and run efficiently. 

#### Context switching
This occurs when \<N> threads run on \<M> logical cores, where M < N.

The CPU **time-shares** between the threads, which means:
- Each thread is given a **small time slice** to execute.
- Once its time slice ends, the thread is **swapped out** of the core, and another thread is **loaded in**.
- This process involves **saving and restoring the thread's state** (registers, memory), which introduces **overhead**.
- **Context switching** is managed by the operating system, not the hardware, so it takes much more time. 

> [!quote] Note:
> **Context switching** must be avoided if possible, because it creates a lot of overhead.


#### Practical examples
Let's clarify the difference even further, exploring how parallel processes and threads can be executed using multiple cores and logical cores:

- **Parallel Processes (OS-Level)**
    - The OS can run **more processes** than the number of physical or logical cores, but:
        - **Up to the number of physical cores**: Tasks can run in true parallel without context switching.
        - **Beyond the number of physical cores**: Tasks will **time-share** the CPU using context switching, which can reduce efficiency.
-  **Parallel Threads (Inside a Process)**
	- **Threads** within a process are scheduled by the OS just like separate processes.
	- The number of threads that run simultaneously:
	    - **Up to the number of logical cores**: Threads will run concurrently (on the same physical core), meaning they can change rapidly and do share the resources efficiently,  or even in parallel (if they are on different physical cores).
	    - **Beyond the number of logical cores**: Threads will run with context switching, being swapped out and loaded back into the CPU, causing an overload and loosing performance

#### GIL
The Global Interpreter Lock (GIL) in CPython (the most common Python implementation) **restricts only one thread of the same process from executing Python bytecode at a time**, even on multi-core systems.

This means that **two Python threads cannot run true parallel**, even on multiple physical cores. They can only run **one at a time**

However, a thread under the GIL **does release control during I/O operations** (e.g., file reading, network requests), so Python can handle **concurrent I/O-bound tasks** effectively.

In fact, threads are constantly (every 5 milliseconds) prompting each other to release the GIL, fighting for it. Whenever running thread gets such a prompt, it has to release the GIL. Then another thread can take control (capture the GIL). The winner is chosen randomly, this depends on the concrete OS. 

The main reason for GIL is thread safety: making sure that only one thread can run at a time inside one process means that threads won't accidently access the same resources at the same time (imagine one thread writing to a file while other is reading from it)

### multiprocessing
Is a standard python module, which allows you to create separate independent processes and run them truly in parallel, utilizing the number of physical cores of your computer.

This can be helpful if you try to solve some heavy CPU-bonded tasks, but only in case they can be split into independent pieces.

>[!quote] Example:  
>Calculate a sum of all elements of a huge list. If your machine has 8 cores, you can "cut" the list into 8 smaller lists and calculate the sum of each of those lists separately on separate core and then just add up those numbers. You'll get a ~8x speedup by doing that.

```python
from multiprocessing import Pool

# Function applied to each element
def square(n):    
	return n * n
	
if __name__ == '__main__':    
# Creating 4 separate processes
	with Pool(processes=4) as pool:        
		values = [1, 2, 3, 4, 5]
		# Apply squaring to all values independently          
		results = pool.map(square, values)        
		print(results)
```

### threading
A standard module allowing you to launch multiple threads. This can be used to utilize the amount of logical cores of the CPU, to run threads concurrently (not in parallel!).
```python
import threading

def f(a, b, c):
    # do something
    pass

t = threading.Thread(target=f, args=(1, 2), kwargs={'c': 3})
# Create a new thread
t.start()
```

Whenever a thread will lock upon some I/O-bond task, it will release GIL, and the other thread could take advantage of that. So threading is a great way to process a numerous amount of incoming connections, by creating a new thread upon each new recieved connection.

### asyncio
Another standard python library, which allows you to **write concurrent code in a single thread**, taking advantage of the event loop to efficiently handle I/O-bound tasks without being limited by the Global Interpreter Lock (GIL).

While asyncio doesn't directly release the GIL, it leverages the event loop to optimize the execution of tasks. 

You can think of event loop as of an effective manager, which keeps an eye on your concurrent tasks (functions), and is able to switch in-between them (by using the `await` keyword) whenever it is benefitial (usually, when some of the functions is getting blocked).

```python
import asyncio 
import random 

async def my_sleep_func(): 
	await asyncio.sleep(random.randint(0, 5)) 
	
async def display_date(num): 
	for _ in range(5): 
	print(f"Task {num}: {datetime.datetime.now()}") 
	await my_sleep_func() 
	
async def main(): 
	await asyncio.gather(display_date(1), display_date(2)) 
	
asyncio.run(main())
```

### Practical reccomendations:
- Multiprocessing → CPU-intensive tasks like matrix multiplications.
- asyncio → for scalable, high-concurrency, non-blocking I/O tasks.
- Threading → `threading` if you have blocking I/O code that cannot be easily converted to async or you need simpler concurrency.

| **Asyncio**                                                                                                                                                                           | **Threading**                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use **asyncio** when your task involves **a lot of I/O-bound operations** (e.g., HTTP requests, database queries) and you need to handle **many connections** **in a single thread**. | Use **threading** when your task involves **I/O-bound operations** but you have **blocking libraries** or tasks that are not designed to be asynchronous. |
| Efficient for **high concurrency** with **low memory usage**.                                                                                                                         | Easier to implement if you don’t want to refactor existing blocking code.                                                                                 |
| **Event loop-based concurrency**.                                                                                                                                                     | **Preemptive concurrency** (managed by OS).                                                                                                               |

What is a blocking operation? Can they be used with asyncio corutines?
?
>[!quote] Definition
> Blocking operation is the operation which stops the entire thread when waiting for execution. `time.sleep()/input()/requests.get()` all are blocking operations, thus they **can not be used as asyncio corutines**, and require multithreading to be handled efficiently.
<!--SR:!2025-02-15,58,310--> 


#🃏/job_questions 
## Key questions

What are the 3 possible states of running multiple processes/threads? Provide a short description of each one.
?
- Parallel running (no switching)
	- Multiple processes/threads are loaded into multiple physical cores and can be executed truly in parallel, independently. This helps to speed up any task which can be parallelized
- Concurrent running (SMT)
	- \<N> threads are loaded into \<N> logical cores within one physical core, and do smart-share it's resources between each other.
		- They can't run in parallel, but can rapidly (in a single clocktime) switch between each other.
		- Both threads stay on the same physical core and are not being swapped out.
		- If one of the threads become idle, the other one takes advantages of it's resources.
- Switching context
	- Number of threads is greater then number of available logical cores, so they have to interchange each other.
		- Each thread is given a small time slice to execute.
		- Then it's being swapped out of the core, another thread is being loaded
		- This process is controlled by OS
		- Swapping causes a great overhead, so should be avoided, if possible
<!--SR:!2025-02-24,65,310-->

What is GIL? How does it limit the parallel running possibilities in python? How do multiple threads interact with GIL?
?
- Global Interpreter Lock - a mechanism allowing only one thread to be executed at a time. Thus, running multiple threads within one CPython process is not possible
- Multiple threads are trying to capture the GIL, prompting each other to release the GIL every 5 milliseconds. Whenever GIL is released, OS scheduler gives it to some thread
<!--SR:!2025-02-19,60,310-->

How do multiprocessing, threading and asyncio libraries allow for efficient multiple task execution?
?
- multiprocessing allows for creation of multiple processes, utilizing the amount of physical cores on your machine, allowing to deal with CPU-bond tasks
- threading allows for creation of multiple threads, utilizing the amount of logical cores on the machine. While not being able to run at the same time (due to the GIL), they might help you if you have some I/O-bonded task (even the blocking one, like `requests.get()`), because the "frozen" thread will be paused, and the resources will be used by another thread.
- asyncio allows for concurrent running of multiple coroutines within a single thread, thanks to the event-loop mechanism. This will work only with non-blocking operations. The advantage is: the number of such coroutines might be much more, than the number of logical cores (there may be thousands of I/O bonded operations).
<!--SR:!2025-02-12,55,310-->


