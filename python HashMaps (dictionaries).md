Make sure you can answer all the questions from [python HashMaps (sets)](python%20HashMaps%20(sets).md) before reading this.

In python, dictionaries do also use HashMaps, but they are built a little different.

### Memory Issue
Let's take a look at the classical realization and figure out what is the issue here:
```python
>>> swimmers = {'Mon': 14, 'Tue': 12, 'Wed': 14, 'Thu': 11}
```
![Pasted image 20241128095958.png](Pasted%20image%2020241128095958.png)
Here you can see a hashmap, with each bucket containing the pointer to the key and to the value. This results into 24 bytes of required memory for each bucket, so the 8-bucket initialized table will consume 192 bytes of memory. As we remember, at least 1/3 (for dictionaries, it's more like 2/3 really) of this memory will stay empty, and that's a big waste

### Optimization
To fight the described issue, a dictionary hashmap is being splitted into 2 parts: **the indexes array and the entries table**

![Pasted image 20241128100727.png](Pasted%20image%2020241128100727.png)
The entries table is being filled one by one, step by step, when the `key:value` pair is added to the dict.  **It's overall size can be no more than 1/3 of indexes array size**, but for now we will draw diagrams like it's 2/3 of the size (so they won't become so big).

The indexes array, on it's own, is initialized with 8 buckets (just like the ordinary hashmap), and doubles it's size whenever entries table has reached it's limit. Buckets do contain '-1' initially, meaning that they are empty. 

This way, the same data we have described will consume only 8 bytes for the index array and 96 (24\*5) bytes for the entry table
![Pasted image 20241128102001.png](Pasted%20image%2020241128102001.png)

### Adding new element 

How are the new dictionary entries added to the hashmap? Describe all the steps
?
Let's describe how the new elements are added to the dictionary:
```python
mydict.update('Mon', 14)
```
1. Calculating the **hash code of the key**
```python
hash('Mon')
```
2. Calculate the index
```python
hash('Mon') % len(indices)
```
1. Сheck the index array bucket at the calculated index
	1. If it contains "-1", the bucket is free and a new entry is added:
	   ![Pasted image 20241128102019.png](Pasted%20image%2020241128102019.png)
	   The index array is updated and is now pointing at the entry inside the entries table.
	2. If it contains anything besides "-1", that means we have run into an index collision. Compare the hash codes of the existing entry key and the key you are trying to add now.
		1. If they are different, increment the index and place the entry into the next empty bucket
		   ![Pasted image 20241128104952.png](Pasted%20image%2020241128104952.png)
		2. If they are the same, this may be a hash collision. Then you should also compare key objects themselves (that's why the keys should have the `__eq__` method implemented)
			1. If key objects are the same, you are trying to add an existing key inside a dictionary. In python, dictionaries are being updated, so the old value is replaced with the new one.
			2. If they are different, increment the index and search for the next empty bucket.
<!--SR:!2025-03-09,14,290-->



### Optimization hint with `__dict__`
By default, all python classes store their attribute values inside dictionaries, where keys are the attribute names, and values are, well, just values.

As you can guess, most part of the object classes do have the same keys, and only values can change from one entry to another.

This fact resulted into some additional optimization step introduced in [PEP 412 - Key-Sharing Dictionary](https://www.python.org/dev/peps/pep-0412/). These are called split-tables

![Pasted image 20241128105713.png](Pasted%20image%2020241128105713.png)

The split-table optimization is most effective when you have a large number of instances of the same class with identical attribute names. This allows Python to share the dictionary keys and hash values among these instances, significantly reducing memory usage

Now, **all different instances do only store compact value arrays.**

> Note: However, if some of the instances has unique additional attributes, a separate classical hashtable will be created for it, reducing the memory and speed efficency


#🃏/job_questions 
## Key questions

What is the size of a single bucket inside a dictionary HashMap?
?
24 bytes (196 bits)
<!--SR:!2025-03-11,16,290-->


What are the indexes array and the entry table? What are their relative lengths? What are their memory consumption? How do they save memory storing dictionaries compared to the classical HashMap?
?
- The classical HashMap is divided into the **indexes array** and the **entry table**. First one do contain indexes-pointer to the second one, and the second one do store key hashes, key pointers, values pointers
  ![Pasted image 20241128100727.png](Pasted%20image%2020241128100727.png)
- Entry table length can be no more than 1/3 of the indexes array, when it reaches it's limit, the indexes array is being doubled.
- Each bucket inside the indexes array consume 8 bits (1 byte) and inside the entry table consume 196 bits (24 bytes).
- **Entry table does not contain blank lines**, like in the classical hashmap, and that's the trick. Indexes array points either to an existing bucket inside the entry table, or holds "-1" value (meaning that the bucket is empty and free to fill).
<!--SR:!2025-03-10,15,294-->


What are the splitted tables introduced for classes in python? How do they save memory? What if some instance has a unique attribute (assigned after initialization, for example)
?
- Splitted tables are used to keep  `attribute:value` pairs for python classes. The class itself stores the index array and the entry table, and it's being shared across all the instances. Instances do only store actual values:
  ![Pasted image 20241128105713.png](Pasted%20image%2020241128105713.png)
- If some instance do has a unique attribute, a classical HashMap will be used for storing it's information instead, which is unefficient. That's why initializing all the attributes inside the `__init__` is highly reccomended.
<!--SR:!2025-03-09,14,294-->









