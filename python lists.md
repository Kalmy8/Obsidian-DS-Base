---
type: note
status: done
tags: [tech/python]
sources:
-
authors:
-
---

#🃏/semantic/data-structures #🃏/job-interview

## Key questions:

What is a python list (under the hood)
?
Talking about CPython (which is the most popular implementation), lists are the **arrays of pointers**, each pointer leads to some object in memory.
<!--SR:!2027-01-05,365,350-->

How is a python list different from the standard C array? What is the reallocate operation? How does it work?
?
Python does provide the **reallocate method**, which allows it to **dynamically change the amount of allocated memory**, if it runs out of space. while adding new elements. The operation is simple: python does creates a new array of bigger size and just copies all of the old array content there.
Note: Array have some Capacity - maximum amount of elements which it can hold without resizing. Then Array is being extended over that point - O(n) resizing happens
<!--SR:!2027-01-05,365,350-->

What are the algorithm complexity for methods:
- Append
- Insert
- Pop
- Remove
?
- Append/pop: O(1)
- Insert/remove: O(n)
<!--SR:!2027-01-05,365,350-->

