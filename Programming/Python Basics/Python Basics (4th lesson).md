---
type: note
status: done
tags: ['tech/python']
sources:
-
- "[[Python Basics Course]]"
authors:
-
---

#🃏/semantic/python #🃏/python-basics-course

**Codewords:** Python's `for` loop, `enumerate` and `range` commands

### "For" loop
First, let's get familiar with **ITERATION**, **ITERATOR**, and **ITERABLE** definitions, as they'll help you understand how loops and generators work in Python. 

**ITERATION** - the general process of accessing elements within a sequence, one by one or in batches.

**ITERATOR** - a Python **object** with a special **`__next__()`** method, enabling iteration through a sequence.

**ITERABLE** - a Python **object** which can be traversed with use of **ITERATOR** Basic Python iterables are **lists, sets, tuples, dictionaries, ranges, str**.

> **Note:** Methods surrounded by double underscores (\_\_) are typically not meant for direct user calls. They're invoked internally by Python as needed.

Let's explore common **`for`** loop usage scenarios:

#### 1.1. Elements Extraction (for)

```python
my_iterable = [1, 2, 3, 4]
for x in my_iterable:
	print(x, end=', ')
# Output: 1, 2, 3, 4 
```
Here, `for` statement implicitly creates an **iterator** for `my_iterable`, which assings each extracted value to `x` until all items are processed. After the loop, `x` retains the last assigned value (**4** in this case).

- **Problem 1:** Print each number from 0 to 4 using a `for` loop and `range()`.
- **Problem 2:** Print each character in the string "Python".

#### 1.2. Modifying the Iterable Itself (enumerate)

```python
my_iterable = [1, 2, 3, 4]
for index, x in enumerate(my_iterable):
	my_iterable[index] += 1

print(my_iterable)
# Output: [2, 3, 4, 5]
```
This example **uses `enumerate` to get both the index and value of each element**, allowing you to modify the original list during iteration.

- **Problem 1:** Print the index and value of each color in `colors = ["red", "green", "blue"]`.
- **Problem 2:** Use `enumerate()` to multiply each number in `numbers = [1, 2, 3]` by its index and print the result. (e.g. 1\*0, 2\*1, 3\*2)

#### 1.3. Executing Code Multiple Times (range)
`range()` creates a sequence of numbers, often used with `for` loops.

* `range(stop)`: 0 up to (but not including) `stop`.
* `range(start, stop)`: `start` up to (but not including) `stop`.
* `range(start, stop, step)`: `start` up to (but not including) `stop`, incrementing by `step`.
```python
for i in range(5): print(i) # 0 1 2 3 4
for i in range(2, 6): print(i) # 2 3 4 5
for i in range(1, 10, 2): print(i) # 1 3 5 7 9
```

**`range()`** is usually used in 2 casses:
- When you need to explicitily create an arithmetic progression: 
```python
for x in range(1, 10, 2):
	print(x, end=', ') 
# Output: 1, 3, 5, 7, 9, 
```

- When you need to repeat some lines of code multiple times:

- **Problem 1:** Print the numbers 10, 12, 14, 16, 18 using `range()`.
- **Problem 2:** Print the numbers 100, 80, 60,..., 0 using `range()`.
- **Problem 3:** Use `range()` to print the multiples of 5 (5, 10, 15..) from 5 to 50 (inclusive).

### Problems (Mixed): Combining for, enumerate, and range

1. Given the string `text = "hello world"`, use a `for` loop and an `if` statement to count the number of spaces in the string.
2. Given a list of names `names = ["Alice", "Bob", "Charlie"]`, use a for loop and `enumerate` to greet each person with their index, like this: "Person 1: Alice", "Person 2: Bob", etc.
3. **Sum of Even Numbers:** Write a program that calculates the sum of all even numbers from 1 to 20 using a `for` loop.
4. **Factorial:** Calculate the factorial of a given number using a `for` loop. (Factorial of 5 = 5x4x3x2x1)
5. **List Reversal:** Reverse a list using a `for` loop and store the reversed elements in a new list.
6. **Pattern Printing:** Print the following pattern using nested `for` loops:
 ```
 1
 12
 123
 1234
 12345
 ```
7. **Vowel Counter:** Write a program that counts the number of vowels in a given string using a `for` loop.

**Review Questions:**

What is the purpose of the `range()` function, and how is it commonly used with `for` loops?
?
`range()` generates a sequence of numbers. It's used with `for` loops to iterate a specific number of times or over a sequence of integers.
<!--SR:!2025-12-17,252,330-->

How does `enumerate()` enhance `for` loops when working with sequences like lists or strings? What two values does `enumerate()` provide on each iteration?
?
`enumerate()` provides both the *index* and the *value* of each item in a sequence, making it very convenient for tasks that require knowledge of the element's position.
<!--SR:!2025-12-04,239,330-->

In a `for` loop using `range(start, stop, step)`, will the loop iterate up to and including the *stop* value or up to but *not including* it? If the *start*, *stop*, and *step* values are not specified when calling the `range` function, what default values will Python use for each?
?
The loop iterates up to, but *not including*, the *stop* value. `range()` with one argument defaults to starting at 0 and uses a step of 1. So `range(5)` is equivalent to `range(0, 5, 1)`.
<!--SR:!2026-02-09,276,330-->

