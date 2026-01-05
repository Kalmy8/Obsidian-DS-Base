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

#🃏/source/python-basics-course

**Codewords:** Compiled and Interpreted programming languages, Python Objects, Immutable and Mutable Data types

## 1. Python
Python is a programming language, thus it has a purpose to translate human-readable commands (e.g. ```print("Hello world")```) to some 0/1 digit mess, which can be executed by a computer.

There are a numerous amount of programming languages, and they are often being divided into 2 groups: **interpreted** and **compiled** ones

Python is often referred as an interpretered programming language. 
Frankly speaking, there is no much sense of relating any modern programming language to a single group, because most part of languages have few different amount of versions and implementations (like IronPython, CPython, PyPy and so on).**It makes more sense to talk about this in a scheme of past history**: long time ago, there was only 2 possible ways how a programming language could work:
- Interpreted language analysis written scripts line by line, translates it into machine code and executes it on fly;
- Compiled language in first place translate all the code to the machine language, and only then allow execution.

Nowadays, there are so much more ways to perform such a task that you **should prioritize understanding a whole process** rather then understand what the termin "interpreted" is. 
Let's compare the typical "compiled" language, such as C#, with Python (CPython - the most popular implementation) 
<br>
![Pasted image 20241117172425.png](../../📁%20files/Pasted%20image%2020241117172425.png) [Take a look at the explained whole process](../Interpreted%20and%20Compiled%20pipeline.md)

According to the given figure, it is hard to tell the difference between interpreted and compiled languages, and that is true! 

Although C# has an **AOT compiler**, which actually translates all the **.IL** code directly to the machine language before execution, it also has **JIT**, which translates code line-by-line right before execution, very likely to how python does so. 

The whole difference here is covered in small nuances on **stage 2** and **stage 3**. For example, one would say that **.IL** compiled file is closer to machine code and compilation proccess is much stricter, and the bytecode is closer to the original code thus can have more errors in it... 
But that's all just some implementation details, so most part of **modern languages can be both compiled and interpreted depending on the concrete implementation!**

## 2. Data types
Data type states some form of knowledge, some structure to keep information and also **all the methods avaliable** to work with that structure. 

So, let's say, *string* object is defined with quote symbols ('str' or "str") and have many methods avaliable for them ('str'.upper() -> 'STR' or
'str' + 'banana' = 'strbanana')

It is helpful to think about all of our programm variables as of some kind of **objects** in computer memory. In fact, you often can come up into phrase that **everything in python is an object, and that's true**.
![Pasted image 20240807150909.png](../../📁%20files/Pasted%20image%2020240807150909.png)

Data types can be either **mutable** or **immutable**, defyining if the related **objects** can or can not be changed in the memory heap.
There are only 3 base data types that **are mutable**, memorize them:
- Lists: \[elem1, elem2,..\]
- Dictionaries: \{keyword : value, keyword2 : value2\}
- Sets: {1,2,3,4}

All other data types **are immutable**. 

> Take a look at the concrete example [here](../Objects%20in%20Python.md) to clarify the difference.

The last thing to say, it is helpful to know that some of the objects are already allocated in heap when the programm launches. That's done for perfomance reasons and they are:
- Some small integers (0,1,2,3...)
- Single-character strings ('a', 'b'...)
- False, True and None objects
- Some other stuff...

**Review Questions:**
What are the key differences between interpreted and compiled languages, and how does Python fit into this classification?
?
- In order to complete the instructions given within the user code Interpreted languages do rely on an interpreter - a program which reads user code line-by-line, converts it into machine code and executes right away.
- Compiled languages do instead firstly convert all the code into the machinery form, and when execute all the instructions at once.
- Python is usually referred as an interpreter language, but it actually has a compilation stage (compiles into bytecode `.pyc` files ), so it's not quite accurate.
<!--SR:!2025-12-08,288,336-->

Describe 4 main stages of the user-code execution process. Which of this processes belong to the compilation stage?
- Lexical analysis: user-written code is being split into certain tokens: variable names, values, functions, control statements etc.
- Parsing: split code is now being gathered into the concrete sequence of instructions which are meant to be done, this structure is known as **Abstract syntax tree**.
- Compilation: Abstract syntax tree is now being converted into a sequence of bytes, known as a **bytecode**. A `.pyc` file containing this bytecode is being created.
- Interpretation: Python Virtual Machine (PVM) now do translates all the bytecode into the machinery code line-by-line and executes it on fly.

What are the `.pyc` files? What role do they play in terms of program execution?
?
`.pyc` (python-chached) files contain python **bytecode**, which is the result of first 3 stages of python code execution pipeline. This files are being cached into the script directory, and are being updated whenever a script is being modified. If there are no changes, PVM will skip first 3 stages and will interprete the bytecode right away, the **resulting performance boost is the reason why `.pyc` files exist**.
<!--SR:!2025-12-25,284,336-->

How are python datatypes categorized? Which datatypes fall into each category?
?
- Mutable: set, dict, list
- Immutable: all the rest ones
<!--SR:!2026-01-11,301,336-->

How do Python represent objects inside the memory heap? Enumerate all the components or draw a diagram.
?
![Pasted image 20240807150909.png](../../📁%20files/Pasted%20image%2020240807150909.png)
<!--SR:!2026-11-28,365,356-->

Name the output of each piece of the given code:
```python
	x = 5
	y = x
	x = 10
	print(y)
	 # OUTPUT HERE EQUALS ?#
	d1 = {'a': [1, 2, 3]}
	d2 = d1.copy()
	d1['a'].append(4)
	print(d2)
	# OUTPUT HERE EQUALS ?#
	a = (1, 2, [3, 4])
	b = a
	a[2].append(5)
	print(b)
	# OUTPUT HERE EQUALS ?#
	# OUTPUT HERE EQUALS ?#
```
?
```python
	x = 5
	y = x
	x = 10
	print(y)
	 # OUTPUT HERE EQUALS 5#
	d1 = {'a': [1, 2, 3]}
	d2 = d1.copy()
	d1['a'].append(4)
	print(d2)
	# OUTPUT HERE EQUALS {'a': [1, 2, 3, 4]}#
	a = (1, 2, [3, 4])
	b = a
	a[2].append(5)
	print(b)
	# OUTPUT HERE EQUALS (1, 2, [3, 4, 5])#
```
<!--SR:!2027-05-07,755,330-->