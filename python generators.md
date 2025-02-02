Must know: [Iterable and Iterator classes](Programming/Iterable%20and%20Iterator%20classes.md)

We can think of generators as of advanced Iterators. Conceptually, an Iterator is an object responsible for traversing some collection. Generator, on other hand, does not only traverse a collection, but can modify or even create new returned values by itself.

Moreover, every generator must implement both `__iter__` and `__next__` methods, just like an ordinal iterator.

There are 2 ways to create generators in python:

### Yield
This is a keyword similar to `return`. The easiest way to understand how the `yield` keyword works is to look at the concrete example:

```python
def gen_fun():    
	print('block 1')    
	yield 1    
	print('block 2')    
	yield 2    
	print('end')

mygen = gen_fun()
for i in mygen:    
	print(i)
```

Let's break down what's happening here into several steps:
- gen_fun() returns a generator object. This objects implements `__next__` and `__iter__` methods under the hood
- `for` statement uses the `iter()` function under the hood accessing the `__iter__` method of the generator object
- `__iter__` method returns the generator itself, the `__next__` method is invoked
- when the `__next__` method is called, we are falling inside the generator function and get "1" as the output:
  ![Pasted image 20241128125816.png](📁%20files/Pasted%20image%2020241128125816.png)
  ![Pasted image 20241128125846.png](📁%20files/Pasted%20image%2020241128125846.png)
  ![Pasted image 20241128125855.png](📁%20files/Pasted%20image%2020241128125855.png)
- when the `__next__` method is called again, we are falling inside the generator function **to the place we have left previously**, execute further code and get "2" as the output:
  ![Pasted image 20241128130036.png](📁%20files/Pasted%20image%2020241128130036.png)
  ![Pasted image 20241128130046.png](📁%20files/Pasted%20image%2020241128130046.png)
  ![Pasted image 20241128130058.png](📁%20files/Pasted%20image%2020241128130058.png)
- when the `__next__` method is called again, we are falling inside the generator function **to the place we have left previously**, execute further code and print "end". No value is returned, so `for` cycle got no `i` and does not execute the loop anymore

The resulting output is:
```python
block 1
1
block 2
2
end
```

### Generator expressions

What are the generator expressions? Why are they used, how are they benefitial from list compehensions?
?
```python
(i for i in range(10000000))
```
Are used for the collections lazy-creation. Here, we are not creating a whole collection of numbers, but rather create objects one by one. That's so simple yet convinient
 

### Yield from
Is used to build nested generators. This statement transfer the program flow to the underlaying generator or iterator object and fetches returned values from there. 

You can use any debugger to traverse this simple example
```python
def base_gen():  
    for i in range(5):  
        yield i  
  
def outer_gen():  
    print('Outer generator is invoked')  
    yield from 'abc'  
    yield from base_gen()  
  
for i in outer_gen():  
    print(i, end = ' / ')  
  
#Outer generator is invoked  
#a / b / c / 0 / 1 / 2 / 3 / 4 /

```

#🃏/job_questions 
## Key questions

Conceptually, what is a generator, how is it different from a iterator?
?
Both of them must implement `__next__` and `__iter__` methods. The difference is: the iterator is only responsible for traversing some collection, while generators can create their own values or modify values they extract


What is the purpose of the yield keyword? What if I call a `__next__` method multiple times on a generator created by yield-containing function?
?
- Yield keyword makes function return a generator instead of a normal value.
	- Whenever you call the `__next__` method on this generator, the function will be executed, from the starting point and all the way up to the `yield` keyword
	- Next time you call `__next__`, the same function will be executed, but not from the beginning, rather than from the point you have hit the `yield` keyword last time
	- This behaviour continues up to the point when the function has completed it's execution and now `yield` keyword is met. When the generator returns no value, and stops it's execution


What is the usage of `yield from` method?
?
`Yield from` keyword is used inside the nested generator objects, allowing you to return values obtained from some sub-generator or sub-iterator like:
```python
def base_gen():  
    for i in range(5):  
        yield i  
  
def outer_gen():  
    print('Outer generator is invoked')  
    yield from 'abc'  
    yield from base_gen()
```






