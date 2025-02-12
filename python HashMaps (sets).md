are the fancy word for a **HashMap/HashTable** - a common data structure popular across many different programming languages.

[python HashMaps (dictionaries)](python%20HashMaps%20(dictionaries).md)
## First view

From the first view, HashMap is just a `key : value` - like structure, allowing you to access elements using hashcodes (instead of using indexes, like you do with a list)

There are 2 reasons why are HashMaps so popular: 
1. Having the ability to use custom keys is amazing and enhance readability a lot
2. The lookup operation is much faster compared to a list (O(1) vs O(n)). This is possible thanks to the hashing mechanism

## Hashing mechanism
The inner logic of a HashMap is simple yet effective, but to make sense of it we should first get familiar with **hashing**. 

Each object in python do has some `__hash__` method, which contains a function capable of calculating a **unique integer value (a hash)** assigned to the object.

### 1. Built-in data types hashes
For default **Hashable** built-in data types , `__hash__` method is pre-defined and outputs the **consistent hash every time the programm runs**. In order to be hashable, an object also needs to provide the `__eq__` method, and **equal objects HAS to have equal hashes**

> Note:
> Since python 3.3, the SipHash security algorithm is used, which results into random hashes for `str, bytes, datetime` data types. This means that hashes are no more consistent while re-running the interpreter.
 
Default objects are: all the immutable objects (including functions) + immutable containers, tuples) if they do only contain immutable objects

### 2. Custom objects default hash
For custom functions and classes, the default hash is based on it's memory address (`id`). And stays consistent through the object's lifetime. 

However, since memory address is assigned differently every time the program runs, the returned hash will also be arbitrary.

### 3. Custom objects custom `__hash__`
To achieve a consistent hash from the custom class, one should define both `__hash__` and `__eq__` methods from that class, and ensure that equal object do return equal hash

### Adding an element to a set
How is the obtained hash used?
Adding new element can be described with an image:
![Pasted image 20241127140845.png](Pasted%20image%2020241127140845.png)

To make thing even simpler, let's provide an actual example of what's happening under the hood when we are trying to do
```python
myset = {'Mon', 'Tue', 'Wed', 'Thu', 'Fri'}
```

#### Step 0: Initializing an empty hash table
Whenever new empty set or dictionary is created, python creates a **HashTable** size of 8 looking as follows:
![Pasted image 20241127135419.png](Pasted%20image%2020241127135419.png)
Rows are called `buckets`, and their size is fixed. Each bucket has it's unique **hash**, and the stored **pointer to one single** element. 

Python automatically tracks the number of empty buckets, and it doubles the size of the hashtable if 2/3 of it becomes filled. It is done due to the optimizations reasons: if hashmap is almost full, all occuring collisions will likely result in a linear search with time complexity O(n), which neglects the main benefit of using hashmaps.

#### Step 1: Calculating hashes
For each element in my set, python now calculates it's hash:
```python
>>> hash('Mon')
4199492796428269555
```

#### Step 2: Calculating the index
When the hash is calculated, we need to place the element inside the hash table, so we need an index.

The index is calculated as the modulus by the size of the hashtable.

```python
>>> 4199492796428269555 % 8
3
```

#### Step 3: Place the pointer inside 
Given the calculated index, we check if we do have an empty bucket, and if so, we add the new entry to the table:
![Pasted image 20241127151535.png](Pasted%20image%2020241127151535.png)

#### Step 4: Repeat and process collisions
The described process is repeated for every new value added to the set, with some additional complexity. 

The problems are: 
- **Different objects, though unlikely, can have the same hash**. This situation is called a hash collision, and this results into same calculated indexes.
- Different hashes, after the modulus operation, can result into same indexes (step 2). This situation is called an index collision.

Whenever one of the situation occures, python handles it with the same logic:
1. Using the `__eq__` method, it checks if the element presented in the hashtable is the same, as the element we are trying to put in. If elements are the same, we should just do nothing. That's why we do need an `__eq__` method for object to be hashable
```python
myset = {'Mon', 'Tue', 'Wed', 'Thu', 'Fri'}
myset.add('Mon')
```
2. If elements are not the same, the index is being incremented by one, and the element is being placed in the next bucket:![Pasted image 20241127152807.png](Pasted%20image%2020241127152807.png)

> Note: Incrementing the index by 1 every time the collision occurs results into an unefficient structure, when hashtable is being sparse with local chains of filled buckets. So, from time to time, python rearranges items inside the hashtable.

### Lookup for an element
```python
>>> 'Tue' in myset
True
```
The lookup logic is practically the same as the adding logic, so we will just name the required steps:
1. Calculate the hash for the lookup element ('Tue')
2. Calculate the index of the element by using the modulus operation
3. Given the index:
	1. If the bucket is empty, return `False`
	2. If the bucket is not empty, compare with the element inside using the `__eq__` method
		1. If elements are equal, return `True`
		2. If not, increment the index and move up to the next bucket. Repeat the process once again
			1. If next bucket is empty (which means that element is not presented anywhere within a hashtable), return `False`


#🃏/job_questions 
## Key questions:

What is a HashMap? What is it's structure?
?
HashMap is a table containing rows (**buckets**). Each bucket does have the same size, the index, the hash code and the corresponding pointer to some object
![Pasted image 20241127135419.png](Pasted%20image%2020241127135419.png)
<<<<<<< HEAD
<!--SR:!2025-02-23,64,310-->
=======

>>>>>>> main

What is hash? How is it calculated for different objects in python.
?
Hash is an integer value - a unique identifier of a python object. Hashes are being calculated differently:
- For python built-in immutable objects, hashing function with sustainable output is used
	- Exceptions are `str/bytes/datetime` objects, for them some randomness is introduced and the output is sustainable only throughout a single interpreter session. Security reasons.
	- For containers (frozensets, tuples) the hash can be calculated only if immutable objects are the inside
- For user custom-defined functions, classes hash is being calculated using the memory address (`id`) of the object, and is being sustainable only throughout a single interpreter session.
	- To enhance sustainability, one must provide `__hash__` and `__eq__` magic methods inside the class.
<!--SR:!2025-02-12,4,276-->


Adding to hashmap/lookup operation complexity
?
Both operations have O(1) complexity
<!--SR:!2025-02-12,4,276-->


How are new elements added to a HashMap? Describe the full process, accounting for the possible hash/index collisions
?
- Calculate the hash for the new object
- Take the modulus using the hashtable width to calculate an index
- If there is no collision, place the pointer to an element by this index
	- If there are the collision, check if objects stored in a bucket is equal to your object
		- If they are equal, do nothing (your element is already presented in a hashtable)
		- If they are unequal, increment the index and move on to the next bucket. Repeat the process
<!--SR:!2025-02-12,4,276-->
 

How are the element being looked up in a hashtable?
?
1. Calculate the hash for the lookup element
2. Calculate the index of the element by using the modulus operation
3. Given the index:
	1. If the bucket is empty, return `False`
	2. If the bucket is not empty, compare with the element inside using the `__eq__` method
		1. If elements are equal, return `True`
		2. If not, increment the index and move up to the next bucket. Repeat the process once again
			1. If next bucket is empty (which means that element is not presented anywhere within a hashtable), return `False`
<!--SR:!2025-02-12,4,276-->


When and how does python increase the size of the hashmap?
?
- Python keeps track of amount of empty buckets, taking care so there will be at least 1/3 of them in a hashmap.
	- Whenever the number of empty buckets lowers to this limit, python doubles the size of the hashmap and copies all the data from the old one to the new one.
		- This is done to performance reasons, otherwise collisions will be processes in O(n) times, which will reduce the speed of the hashmap a lot
<!--SR:!2025-02-12,4,276-->



