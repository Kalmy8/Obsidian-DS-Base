is a mechanism to safely and effectively handle communications with external data-sources, by executing additional logic before and after the communication. They are most commonly used to close the connections appropriately, releasing the recruited resources.

### Usage examples

Managing context can be used when **working with files**, this leads to automatic call to ```file.close()``` method when the rest of the logic is done

```python
with open("file.txt", "r") as file:    
	content = file.read()    
	print(content)
# Implicitly closes the file
```

Database queries:

```python
import sqlite3
	with sqlite3.connect('example.db') as conn:    
	cursor = conn.cursor()    
	cursor.execute('SELECT * FROM table_name')    
	result = cursor.fetchall()    
	print(result)
# Implicitly closes the DB connection
```

Working with threads:

```python
import threading

# Create the lock object once, outside of the worker function.
lock = threading.Lock() 

def worker(): 
# Acquire the lock within the context manager, ensuring safe resource access with lock: 
	with lock:
		print("Working...") 

# Create and start the thread 
t = threading.Thread(target=worker) 
t.start()
```
Here we use context manager to safely and correctly lock a working thread within the worker function.

Net connections:

```python
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
	s.connect(('example.com', 80)) 
	s.sendall(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')  
	response = s.recv(1024)    
	print(response.decode())
# Implicitly closes the created socket
```

### Customized usage

In order to work with managing context, a class should implement `__enter__` and `__exit__` magic functions. 
- First one is executed, when we enter the context manager
- The second one is executed, when we leave it

```python
class Timer:    
	def __enter__(self):        
		self.start_time = time.time()        
		return self        
	
	def __exit__(self, exc_type, exc_val, exc_tb):        
		elapsed_time = time.time() - self.start_time        
		print(f"Elapsed time: {elapsed_time} seconds")
		
with Timer() as timer:       
	time.sleep(2)
```

The other interesting options is implementing the **asynchronous** context manager, which will **work correctly when used with asyncio coroutines**, this can be done by implementing `__aenter__/__aexit__` magic function.

```python
import asyncio

class AsyncTimer:    
	def __aenter__(self):        
		self.start_time = asyncio.get_event_loop().time()
		return self        
		
	def __aexit__(self, exc_type, exc_val, exc_tb):        
		elapsed_time = asyncio.get_event_loop().time() - 
		self.start_time        
		print(f"Elapsed time: {elapsed_time} seconds")
		
async def example():    
	async with AsyncTimer() as timer: 
		await asyncio.sleep(2)
		
asyncio.run()
```

#🃏/job_questions 
## Key questions:

What is the syntax of managing context in python? What are the common usage scenarios?
?
```python
with X as Y:
	do

# Usage scenarious:
# files: with open(filepath, mode) as file
# DB connections: with sqlite.connect(..) as connection
# Net connections: with socket.socket(..) as socket:
# Thread locks: with threading.Lock() as lock:
```
<!--SR:!2025-01-03,15,290-->


How to make custom class work with the context manager? How to use context manager with asyncio coroutines?
?
- To make custom class compatible with context manager, we should implement `__enter__` and `__exit__` class methods.
	- The first one is being called when we enter the managing context
	- The second one is called when we leave
- if "aX" class has `__aenter__/__aexit__` methods implemented:
  ```python
  async with aX as Y:
      # Do asynchronous stuff...
  ```
<!--SR:!2025-01-02,14,290-->