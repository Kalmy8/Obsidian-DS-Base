**Codewords:** User-defined functions, default parameter, typing, args and kwargs.

### Basic function usage.
User-defined functions (methods) are invoked and work just like the standard built-in ones (e.g., `len()`, `sum()`), but have customizable behavior. They are used to prevent you from **repeating yourself**, providing a convenient way to execute some task effectively. Whenever you can detect a common operation within your app, you should probably apply a function for it.

**Example:**
```python
# First line states function's name and parameters
def say_hello(name, surname):
    # This part is called 'function body'
    print('Hello, I am a Python function.')
    print(f'Nice to meet you {name} {surname}!')

# Functions are invoked by their name
say_hello('Alexey', 'Kalmy8')
# Output: 'Hello, I am a Python function.'
# Output: 'Nice to meet you Alexey Kalmy8!'
```

Here, you define a function named **say_hello**, and state that it will accept 2 parameters: **name** and **surname**. Then you can **invoke** this function from any part of your application, passing these parameters, so the function can print them.

Moreover, functions can also use parameters defined outside the function's body:

```python
weather_state = 'Fine'

def say_hello(name, surname):
    print('Hello, I am a Python function.')
    print(f'Nice to meet you {name} {surname}!')
    print(f'The weather is {weather_state}')

say_hello('Alexey', 'Kalmy8')
# Output: 'Hello, I am a Python function.'
# Output: 'Nice to meet you Alexey Kalmy8!'
# Output: 'The weather is Fine'
```

> The reverse logic is not applicable, so you cannot access parameters defined inside your function from the outside.

Our function now just prints the passed parameters to the console, which is nice but not very helpful. Let's define a function which will actually do some computational work and **return the calculated result**:

```python
# First line states function's name and parameters
def summator(a, b):
    # This part is called 'function body'
    result = a + b
    return result

# Calling summator(..,..) with parameters now will result
# in the calculated value
print(summator(3, 4))
# Output: 7

my_result = summator(5,5)
print(my_result)
# Output: 10
```


### Introducing type hints/docs.
There is a little issue with our `summator` function: for now, it can accept any arguments we pass, even if they make no sense. For example:

```python
def summator(a, b):
    result = a + b
    return result

print(summator('somestring', 4))
# Output: TypeError: can only concatenate str (not "int") to str
```

When you are working on a large application, it is impossible to memorize all functions and their usage details, thus there is a great chance to use some function in an inappropriate way/pass some mismatching parameters. We have 2 instruments to address this problem:

###### Type hints: these are little helpers which advise you about what **variable types** the function expects from the user.  
```python
# Types of:     param1   param2   return_value
def summator(a : int, b : int) -> int:
    result = a + b
    return result

print(summator('somestring', 4))
# While execution will still crash, your IDE will
# warn you about the incorrect usage of this function
```

See? Now the function clearly states that it expects you to pass two **integers** and return an **integer** as well.

###### Docstrings: this is an comprehensive description of what the function does, what arguments it should accept, and what value it should return. 
This description can be included right on top of the function's body:
```python
def summator(a : int, b : int) -> int:
    '''
    This function accepts 2 integers and returns their sum.
    Example: summator(3,2) -> 5
    '''
    result = a + b
    return result

print(summator('somestring', 4))
# Output: TypeError: can only concatenate str (not "int") to str
```

Moreover, if you are working with a modern IDE like PyCharm/Visual Studio, this docstring will pop up every time you hover the cursor over your function's name.

**Best Practice:** **You should always use type hints inside your applications, and if a function is at least a little unobvious/complex, you should likely use a docstring for it as well**. It is crucial for applications developed over weeks/months, since you will not memorize all function parameters and their meaning by yourself and will waste a lot of time recalling them again and again.
> Nowadays it is not necessary to do this work yourself. Try asking ChatGPT to write docstrings for your code, and be sure that it will deal with this task well. 

**Problem:** Define a function `greet` that takes a string and returns a greeting message. Use type hints and docstrings for this one.

```python
def greet(name: str) -> str:
    """
    This function takes a person's name as input and returns a greeting message.

    Example:
    greet("Alice") -> "Hello, Alice!"
    """
    return f"Hello, {name}!"
```

### Introducing default parameters:
Default parameters allow you to specify a default value for a function parameter. If the caller doesn't provide a value for that parameter, the default value will be used.

**Problem:** Define a function with default parameters:
Define a function `welcome_message` that has a default parameter for the language, and prints a message based on that language.

```python
def welcome_message(name: str, language: str = "English") -> None:
  """Prints a welcome message in the specified language.

  Args:
    name: The name of the person to welcome.
    language: The language to use for the welcome message. 
               Defaults to "English".
  """

  if language == "English":
    print(f"Hello, {name}! Welcome!")
  elif language == "Spanish":
    print(f"¡Hola, {name}! ¡Bienvenido!")
  else:
    print(f"Welcome, {name}!")

welcome_message("Alice") # Output: Hello, Alice! Welcome!
welcome_message("Bob", language="Spanish") # Output: ¡Hola, Bob! ¡Bienvenido! 
```

### Introducing `*args` and `**kwargs`:

* `*args`: allows you to pass a variable number of positional arguments to a function.
* `**kwargs`: allows you to pass a variable number of keyword arguments to a function.

**Problem:** Define a function `max_of_numbers` that takes any number of integer arguments and returns the maximum value.

```python
def max_of_numbers(*args: int) -> int:
  """Returns the maximum value among the given integers.
  """
  if not args:
    return None  # Or raise an exception
  max_value = args[0]
  for num in args[1:]:
    if num > max_value:
      max_value = num
  return max_value

print(max_of_numbers(1, 5, 3, 9, 2))  # Output: 9
```

**Problem:** Create a function `describe_person` that accepts any number of keyword arguments and prints them as a description.

```python
def describe_person(name: str, **kwargs) -> None:
  """Prints a description of a person based on the given keyword arguments.

  Args:
    name: The name of the person.
    **kwargs: Arbitrary keyword arguments describing the person.
  """
  print(f"Description of {name}:")
  for key, value in kwargs.items():
    print(f"- {key}: {value}")

describe_person("Alice", age=30, city="New York", profession="Engineer")
```

**Problem:** Define a function `order_food` that accepts a default food item, any number of toppings (args), and some special instructions as keyword arguments (kwargs).

```python
def order_food(food: str = "Pizza", *toppings: str, **special_instructions) -> None:
  """Prints an order confirmation with the given food, toppings and special instructions.
  """

  print(f"You ordered a {food} with:")
  for topping in toppings:
    print(f" - {topping}")

  if special_instructions:
    print("Special instructions:")
    for key, value in special_instructions.items():
      print(f" - {key}: {value}")

order_food("Burger", "Cheese", "Bacon", extra_sauce=True, no_pickles=True)
```

#🃏/data-science
### Key Questions:

Define a function `multiply` that takes two integers and returns their product. Use type hints.
?
```python
	def multiply(num1: int, num2: int)->int:
		return num1*num2
```
<!--SR:!2025-02-11,52,310-->

Define a function `power` that takes a number and raises it to a power. The power should have a default value of 2.
?
```python
	def power(num1: int, num2: int = 2)->int:
		return num1**num2
```
<!--SR:!2025-02-18,59,310-->

Define a function `greet` that takes the name of the user, and, optionally, takes the weather state. When it greets the user and also prints the weather state if it's given
?
```python
	def greet(name: str, weather:str = None): 
		print(f"hello {name}")
		
		if weather: 
			print(f"The weather today is {weather}")
```
<!--SR:!2025-02-13,54,310-->


Create a function `sum_integers` that takes any number of integers and prints their sum?
?
```python
	def sum_integers(*integers : int):
		print sum(integers)
```
<!--SR:!2025-03-26,67,322-->


Define a function `print_kwargs` that takes any number of keyword arguments and prints them.
?
```python
def print_kwargs(**kwargs): 
	"""
	Prints keyword arguments passed to the function.
	
	Args: **kwargs: Arbitrary keyword arguments. 
	""" 

	for key, value in kwargs.items(): 
		print(f"{key}: {value}") 

# Example Usage 
print_kwargs(name="Alice", age=30, city="New York") 
# Output: 
# name: Alice 
# age: 30 
# city: New York 

print_kwargs(country="USA", language="English") 
# Output: 
# country: USA 
# language: English
```
<!--SR:!2025-02-03,16,304-->

Define a function `create_message` that takes a default greeting and any number of names (`args`), then prints a greeting for each name.
?
```python
def create_message(greeting="Hello", *names): 
	"""
	Prints a greeting message for each name. 

	Args: greeting: The greeting message (default is "Hello"). 
	*names: A variable number of names. 
	""" 

	for name in names: 
		print(f"{greeting}, {name}!") 
		
# Example Usage 
create_message("Hi", "Alice", "Bob", "Charlie") 
# Output: 
# Hi, Alice! 
# Hi, Bob! 
# Hi, Charlie! 

create_message("Good morning", "David") 
# Output: 
# Good morning, David!
```
<!--SR:!2025-02-04,17,304-->

