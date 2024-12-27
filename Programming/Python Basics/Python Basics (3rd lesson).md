**Codewords:** Python complex data types (dict, tuple, set), their usage and methods.

### **1. Python dictionaries**
Dictionary is yet another **MUTABLE** python data type, think of it as of a typical list, but capable of using *keys* in addition of using just *indexes*.

```python
# Let's create a dictionary
my_dictionary = {'1' : 'First_element',
				 'some_other_key' : 2,
				 4 : ['strings','strings2']}

print(my_dictionary['1'],
	  my_dictionary['some_other_key'],
	  my_dictionary[4], sep = '\n')

# Output: 
'First_element'
2
['strings', 'strings2']
```

Dictionaries are broadly used to store any kind of information which can be associated with *keys*, concrete examples will be given further. 

Note: Only **IMMUTABLE** (e.g. hashable) data types can be used as dictionary keys. For example, you can not create a dictionary record passing a list as a *key*:
```python
my_dictionary = {['I am a list'] : 5,
				 {'i am a set', 'so no hashable'} : 3}

# Output: Error
```

Now let's take a look at some data type **methods** and solve few corresponding problems.

```python
# Let's create a dictionary
my_dictionary = {'1' : 'First_element',
				 'some_other_key' : 2,
				 4 : ['strings','strings2']}

print(my_dictionary.keys(),
	  my_dictionary.values(),
	  my_dictionary.items(), sep = '\n')
	  
# Output: 
dict_keys(['1', 'some_other_key', 4]) # Keys
dict_values(['First_element', 2, ['strings','strings2']]) # Values
dict_items[(1, 'First_element', 
		  ('some_other_key', 2),
		  (4, ['strings','strings2'])) # Items

# "Appending" to a dictionary
my_dictionary.update({'new_record' : 5})
my_dictionary.update(('another_one', 6))

print(list(my_dictionary.items())[-2:])
# Output:
[('new_record', 5),
 ('another_one', 6)]

# Deleting from a dictionary
my_dictionary.pop('1')
print(list(my_dictionary.items())[:2])
# Output:
[('some_other_key', 2),
 (4, ['strings','strings2'])

# Setting the default value
new_dict = {'a' : 10}
new_dict.setdefault('b')
# {'a' : 10, 'b' : None}
new_dict.setdefault('c', 4)
# {'a' : 10, 'b' : None, 'c' : 4}
new_dict.setdefault('a', 3)
# {'a' : 10, 'b' : None, 'c' : 4}
new_dict.setdefault('d', [])
# {'a' : 10, 'b' : None, 'c' : 4, 'd' : []}

```

**Problems**:
- You have the following dictionary representing a simple phone book: `{"John": "123-4567", "Jane": "987-6543", "Jake": "555-4321"}`. Add a new entry for "Jill" with the phone number "777-8888", and then print the updated dictionary.
- You have a dictionary `inventory` that tracks the stock of items in a store: `inventory = {"apple": 5, "banana": 3}`. Use `setdefault()` to ensure that the item "orange" is in the dictionary with a starting stock of 0. Then, update the stock of "orange" to 10 and print the updated inventory.

### **2. Python tuples**
Python tuple is a **IMMUTABLE** data type for storing ordered objects. Tuple is being very similar to list and has the same indexing, but has less methods (as you can not append or pop to/from a tuple) and being a little bit faster.

Tuples are not used so often as other basic data types, but you will run into them from time to time. For example, they can be used for simultaneous variable assignment:
```python
a, b = ('first_value', 'second_value')
```

**Problems**:
- Create a tuple containing the names of three cities: "New York", "Los Angeles", and "Chicago". Retrieve and print the second city from the tuple.

### **3. Python sets**
Python set is a **MUTABLE** data type for storing unordered, unique objects. Think of a set as of a mathematical object: they do share all the same methods (union, intersection, difference and so on). They are also often used for duplicates elimination

```python
# Creating a set 
my_set = {'apple', 'banana', 'cherry'}

# Adding and removing elements 
my_set.add('date') 
print(my_set) 
# Output: {'apple', 'banana', 'cherry', 'date'}

my_set.remove('banana') 
print(my_set) 
# Output: {'apple', 'cherry', 'date'} 

# Eliminating duplicates
duplicator_list = ['a', 'b', 'a']
print(set(duplicator_list))
# Output: {'a','b'}
print(list(set(duplicator_list)))
# Output: ['a','b']

# Union, intersection, and difference 
set_a = {1, 2, 3} 
set_b = {3, 4, 5} 
print(set_a.union(set_b)) 
# Output: {1, 2, 3, 4, 5}
print(set_a.intersection(set_b)) 
# Output: {3} 
print(set_a.difference(set_b)) 
# Output: {1, 2}
```

**Problems**:
- Create a set containing the numbers 1, 2, 3, 4, and 5. Then, remove the number 3 from the set and print the updated set.
- Given two sets of numbers: `set_a = {1, 2, 3, 4, 5}` and `set_b = {4, 5, 6, 7, 8}`, find the difference between `set_a` and `set_b` (i.e., elements that are in `set_a` but not in `set_b`). Print the result.

#🃏/data-science
## Review Questions:
Create a dictionary to store the names and ages of three people: "Alice" (25), "Bob" (30), and "Charlie" (35). Then, retrieve and print Bob's age.
?
```python
people = {"Alice": 25, "Bob": 30, "Charlie": 35}
print(people["Bob"])  # Output: 30
```
<!--SR:!2025-02-14,55,310-->

Given this dictionary:  `data = {"a": 1, "b": 2, "c": 3}`, print all the keys of this dictionary.
?
```python
data = {"a": 1, "b": 2, "c": 3}
keys = data.keys()
print(keys) #Output dict_keys(['a', 'b', 'c'])
```
<!--SR:!2025-02-10,51,310-->

Implement a **frequency counter** with a dictionary `counts` where keys are characters in the string "abracadabra" and values are the count of each character.
?
```python
counts = {}  
for bukva in 'abracadabra':  
    counts.setdefault(bukva, 0)    
    counts[bukva] += 1
print(counts)
```
<!--SR:!2025-01-01,11,234-->

You have a tuple representing a date: `(2024, 8, 21)`. Extract the year, month, and day into separate variables and print them.
?
```python
date = (2024, 8, 21)
year, month, day = date
print(year)   # Output: 2024
print(month)  # Output: 8
print(day)    # Output: 21
```
<!--SR:!2025-01-24,33,292-->

Given two sets: `set1 = {1, 2, 3, 4}` and `set2 = {3, 4, 5, 6}`, find the intersection of these sets and print the result.
?
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1.intersection(set2) 
print(intersection)  # Output: {3, 4}
```
<!--SR:!2025-02-20,60,312-->

You are managing a list of students and their grades, where the data is stored in a dictionary. The dictionary currently looks like this: `grades = {"Alice": [85, 90], "Bob": [78]}`. Add a new student "Charlie" with an initial empty list of grades using `setdefault()`, and then add a grade of 92 for "Charlie". Print the updated dictionary.
?
```python
grades = {"Alice": [85, 90], "Bob": [78]}
grades.setdefault("Charlie", []).append(92) 
print(grades)  # Output: {'Alice': [85, 90], 'Bob': [78], 'Charlie': [92]}
```
<!--SR:!2025-02-24,64,312-->

You have a list of numbers with some duplicates: `[10, 20, 10, 30, 40, 30, 50]`. Convert this list to a set to eliminate duplicates, and then find the difference between the resulting set and the set `{20, 30}`. Print the final result.
?
```python
numbers = [10, 20, 10, 30, 40, 30, 50]
unique_numbers = set(numbers)
difference = unique_numbers.difference({20, 30})  
print(difference)  # Output: {40, 10, 50} (order may vary)
```
<!--SR:!2025-01-23,32,292-->



