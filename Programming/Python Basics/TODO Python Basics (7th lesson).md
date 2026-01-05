---
type: note
status: inbox
tags: ['tech/python']
sources:
-
- "[[Python Basics Course]]"
authors:
-
---

#🃏/source/python-basics-course

**Codewords**: Lambda Functions, `functools` library, `map()`

TODO zip, sorted, join

### Lambda Functions
Lambda functions are small, anonymous functions defined using the `lambda` keyword. They are especially useful for short, simple operations.

```python
square = lambda x: x * x # Example: A lambda function to square a number
print(square(5)) # Output: 25
```

**In-Lecture Problem 1:** Write a lambda function that takes two numbers and returns their sum.

### `map()`

The `map()` function applies a function to every item in an iterable (like a list, tuple, or string) and returns an iterator.

```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x * x, numbers) 
print(list(squared)) # Output: [1, 4, 9, 16] (Convert the map object to a list to see the results)
```

**In-Lecture Problem 2:** Use `map()` and a lambda function to convert the list of strings `["1", "2", "3"]` to a list of integers.

### `sorted()`
- Returns a **new sorted object** without modifying the original collection
- Uses [[OOP Basics (6th) lesson|magic methods]] `__lt__` (less than) and `__eq__` (equals). 
	- **Minimum requirement** is implemented `__lt__` descriptor

**Example:**
```python
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words)
print(sorted_words) # ['apple', 'banana', 'cherry']
```
- `sorted()` allows for **custom sorting logic** by supporting the `key` parameter 
	- `key` parameter must be a **function of element**, returning the rank

```
# Sort by string length
words = ["Python", "is", "awesome"]
words.sort(key=lambda x: len(x))
print(words) # ['is', 'Python', 'awesome']

```
- `key` parameter could accept a function returning several values (in form of collection). **This would allow for sorting collections based on several criteria** (from higher to lower priority)

```python
people = [
 {"name": "Alice", "age": 25},
 {"name": "Bob", "age": 30},
 {"name": "Charlie", "age": 25}
]

# Sort by age, then by name
people.sort(key= lambda x: (x["age"], x["name"]))
print(people)
# Output:
# [{'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 25}, {'name': 'Bob', 'age': 30}]
```

**Practical Problems:**

- Sort positive and negative numbers by their absolute value:
```python
numbers = [-3, 2, -1, 4]
numbers.sort(key = lambda x: abs(x))
print(numbers) # [-1, 2, -3, 4]
```

- Sort a list of strings by their last character:
```python
words = ["apple", "banana", "kiwi", "cherry"]
words.sort(key=lambda x: x[-1])
print(words) # ['banana', 'kiwi', 'apple', 'cherry']
```

- Sort a list of students by math grade, then by science grade:
```python
students = [
 {"name": "Alice", "grades": {"math": 90, "science": 85}},
 {"name": "Bob", "grades": {"math": 80, "science": 95}},
 {"name": "Charlie", "grades": {"math": 90, "science": 80}}
]

students.sort(key=lambda x: (x["grades"]["math"], x["grades"]["science"]))
print(students)

# Output:
# [{'name': 'Bob', 'grades': {'math': 80, 'science': 95}},
# {'name': 'Charlie', 'grades': {'math': 90, 'science': 80}},
# {'name': 'Alice', 'grades': {'math': 90, 'science': 85}}]
```

### `functools.reduce()`

`reduce()` applies a function of two arguments cumulatively to the items of a sequence, from left to right, so as to reduce the sequence to a single value.

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers) 
print(product) # Output: 24 (1 * 2 * 3 * 4)
```

**In-Lecture Problem 3:** Use `reduce()` to find the maximum value in a list of numbers. (Hint: Your lambda function should take two arguments and return the larger one).

### `functools.singledispatch` and `singledispatchmethod`

`@singledispatch` transforms a function into a single-dispatch generic function. This allows you to define different behaviors based on the type of the first argument. Since Python 3.8, you can also use `@singledispatchmethod` to create overloaded methods. It serves the exact same purpose as its function counterpart but applies to class methods.

```python
from functools import singledispatch

@singledispatch
def process_data(data): # Default implementation for unsupported types
 print(f"Processing generic data: {data}")

@process_data.register(int) # Specialized for int
def _(data): # The name of this inner function doesn't matter; we use "_"
 print(f"Processing integer: {data}") 

@process_data.register(list) # Specialized for list
def _(data):
 print("Processing list:", data)

process_data(10) # Output: Processing integer: 10
process_data("hello") # Output: Processing generic data: hello
process_data([1, 2]) # Output: Processing list: [1, 2]

#Example with singledispatchmethod
class DataProcessor:
 @singledispatchmethod
 def process(self, data):
 raise NotImplementedError("Unsupported type")

 @process.register(int)
 def _(self, data: int):
 return f"Processing integer: {data}"

 @process.register(str)
 def _(self, data: str):
 return f"Processing string: '{data}'"

processor = DataProcessor()
print(processor.process(10)) # Output: Processing integer: 10
print(processor.process('hi')) # Output: Processing string: 'hi'
```

**Problem**: 
Write a function called **`describe_data`** using @singledispatch that:
	- Prints "It's a number!" if given an integer.
	- Prints "It's some text!" if given a string.
	- Prints "Unknown data type!" for any other type.

### `functools.partial`

`partial()` creates a new function where some of the arguments of an existing function are pre-filled.

```python
from functools import partial

def greet(greeting, name):
 print(f"{greeting}, {name}!")

greet_hello = partial(greet, "Hello") #The parameter greeting of greet(..) now always has a value of "Hello".

greet_hello("Alice") # Output: Hello, Alice!
greet_hello("Bob") # Output: Hello, Bob! 
```

**Problem:** 
 - Create a function multiply(x, y) that returns the product of x and y.
 - Use partial to create a new function called double that always multiplies by 2.

### `functools.cache` and `functools.lru_cache`

**Caching can significantly speed up function calls by storing the results.** 

The `@lru_cache` decorator provides a least-recently-used cache. 

**@functools.lru_cache(maxsize=128, typed=False):**
- **LRU (Least Recently Used) Cache:** This decorator implements a cache that stores a limited number of recent function calls. The maxsize parameter determines the maximum number of results to store. When the cache is full and a new result needs to be added, the least recently used item is discarded to make space.
 - **maxsize Argument:**
 - **maxsize=128 (default):** The cache can store up to 128 different results.
 - **maxsize=None:** **Equals to @functools.cache**. The cache will grow without bound. Be careful with this, as it can consume a lot of memory if the function is called with many different arguments.
 - **maxsize=0** effectively disables the cache.
 - **typed Argument:**
 - **typed=False (default):** Function arguments of different types will be treated as equivalent for caching purposes if their values are the same. For example, **`f(3)`** and **`f(3.0)`** will be considered the same call and will return the same cached result.
 - **typed=True:** Arguments of different types are cached separately. f(3) and f(3.0) will have their own cached results.

**Example:**
```python
import time from functools import lru_cache 
# 1. Factorial without caching 
def factorial_no_cache(n): 
	if n == 0: 
		return 1 
	else: 
		return n * factorial_no_cache(n - 1) 
		
# 2. Factorial with lru_cache 

@lru_cache(maxsize=None) 
def factorial_with_cache(n): 
	if n == 0: 
		return 1 
	else: return n * factorial_with_cache(n - 1) 
	
# --- Test and Time the Functions --- 
# Without caching 
start_time = time.time() 
print(f"Factorial (no cache) of 5: {factorial_no_cache(5)}") print(f"Factorial (no cache) of 8: {factorial_no_cache(8)}") print(f"Factorial (no cache) of 5: {factorial_no_cache(5)}")

# Repeat calculation 
end_time = time.time() 
print(f"Time taken (no cache): {end_time - start_time:.6f} seconds") 
print("-" * 20)

# With caching 
start_time = time.time() 
print(f"Factorial (cached) of 5:{factorial_with_cache(5)}") 
print(f"Factorial (cached) of 8: {factorial_with_cache(8)}") 
print(f"Factorial (cached) of 5: {factorial_with_cache(5)}") 

# Cached result 
end_time = time.time() 
print(f"Time taken (with cache): {end_time - start_time:.6f} seconds")
```

## Key questions

What is a lambda function? Write one that cubes a number.
?
A lambda function is a small anonymous function.
```python
cube = lambda x: x ** 3 
```
<!--SR:!2025-12-22,257,330-->

How does `map()` work? Write one to square each element in `[1, 2, 3]`.
?
`map()` applies a function to each element of an iterable.
```python
squared = list(map(lambda x: x*x, [1, 2, 3]))
```
<!--SR:!2026-11-28,365,350-->

Explain `functools.reduce()`. Write one to sum the numbers in `[1, 2, 3, 4]`.
?
`reduce()` applies a function cumulatively to an iterable's items.
```python
from functools import reduce
sum_of_elements = reduce(lambda x, y: x + y, [1, 2, 3, 4]) 
```
<!--SR:!2026-02-08,275,330-->

What is the purpose of `functools.singledispatch` and `functools.singledispatchmethod`?
?
It creates a generic function/method that behaves differently based on the first argument's type.
<!--SR:!2026-01-03,266,330-->

Using functools.singledispatch, create a function called get_info that returns the following:
- For an integer, return the square of the integer.
- For a string, return the string repeated twice (e.g., "hello" becomes "hellohello").
- For any other type, return None.
?
```python
	from functools import singledispatch
	
	@singledispatch
	def get_info(data):
	 return None
	
	@get_info.register(int)
	def _(data):
	 return data * data
	
	@get_info.register(str)
	def _(data):
	 return data + data
	
	# Example Usage:
	print(get_info(5)) # Output: 25
	print(get_info("hello")) # Output: hellohello
	print(get_info(3.14)) # Output: None
```
<!--SR:!2025-12-10,245,330-->

How does `functools.partial` simplify function usage? Make a function that always adds 5 using `partial()`.
?
It allows creating new functions with some arguments pre-filled.
```python
from functools import partial

def add(x, y):
 return x + y

add_five = partial(add, 5) 
```
<!--SR:!2026-02-12,279,330-->

What is the use of `@lru_cache`. What arguments does lru_cache accept, how do they affect the caching mechanism? Write a function to effectively calculate the factorial using cache
?
- Caches results of expensive function calls, greatly speeding up repeated executions by storing already computed results.
- Max_size (int): number of last calls which will be memorized
- Typed (bool): whether to treat **func(3)** and **func(3.0)** calls equal
<!--SR:!2025-12-21,256,330-->

**@lru_cache problem:**
- Create a function fibonacci(n) that calculates the Nth Fibonacci number recursively (without caching)
- Add the @lru_cache decorator to the function.
- Call fibonacci(5) twice and observe the output. Notice that the calculation is only performed once.
?
```python
 from functools import lru_cache
 
 @lru_cache(maxsize=None)
 def fibonacci(n):
 if n <= 1:
 return n
 print(f"Calculating fibonacci({n})") # To see when it's actually calculating
 return fibonacci(n - 1) + fibonacci(n - 2)
 print(fibonacci(5)) # Much faster now! 
```
<!--SR:!2026-05-20,350,359-->

How many comparison methods need to be implemented for sorting?
? 
- Only one (usually `__lt__`) is required. Python can infer other comparisons automatically

What's the output of the **`sorted()`** method?
?
- A newly created collection with re-ordered elements

Sort this list of tuples, using the tuple's second element, then first element: data = [(1, 3), (2, 1), (3, 2)]
?
- sorted_data = sorted(data, key=lambda x: (x[1], x[0]))

