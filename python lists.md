#🃏/job_questions 
## Key questions:

What is a python lists work under the hood?
?
Talking about CPython (which is the most popular implementation), lists are the **arrays of pointers**, each pointer leads to some object in memory.
<!--SR:!2025-02-25,66,310--> 

How is a python list different from the standard C array? What is the reallocate operation? How does it work?
?
Python does provide the **reallocate method**, which allows it to **dynamically change the amount of allocated memory**, if it runs out of space. while adding new elements. The operation is simple: python does creates a new array of bigger size and just copies all of the old array content there.
<!--SR:!2025-02-18,59,310-->

What are the algorithm complexity for methods:
- Append
- Insert
- Pop
- Remove
?
- Append/pop: O(1)
- Insert/remove: O(n)
<!--SR:!2025-02-14,57,310-->


