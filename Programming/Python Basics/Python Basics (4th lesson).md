#🃏/programming/python 
**Codewords:** Python's `while` and `for` loops, `enumerate`, `continue`, `break` commands.

**Review Questions:**
- What is the difference between an *iterable* and an *iterator*?
- What happens to the loop variable after a `for` loop finishes execution?
- How can you modify elements within an iterable while iterating over it?

### **1. "For" loop**

First, let's get familiar with **ITERATION**, **ITERATOR**, and **ITERABLE** definitions, as they'll help you understand how loops and generators work in Python. 

**ITERATION** - the general process of accessing elements within a sequence, one by one or in batches.

**ITERATOR** - a Python **object** with a special **`__next__()`** method, enabling iteration through a sequence.

**ITERABLE** - a Python **object** with either a **`__iter__()`** method (returning an **ITERATOR**) or a **`__getitem__()`** method. Basic Python iterables include **lists, sets, tuples, dictionaries, ranges, str**.  The use of **`__getitem__`** for iteration is primarily for backward compatibility with older code or specialized cases. If an object has **`__getitem__`** but no **`__iter__`**, Python will attempt to create a default iterator that accesses elements sequentially by index using **` __getitem__`**. However, this is not the preferred or recommended approach for new code.

> **Note:**  Methods surrounded by double underscores (\_\_) are typically not meant for direct user calls. They're invoked internally by Python as needed.

Let's explore common **`for`** loop usage scenarios:

#### 1.1. Elements Extraction

```python
my_iterable = [1, 2, 3, 4]
for x in my_iterable:
	print(x, end=', ')
# Output: 1, 2, 3, 4 
```

Here, an **iterator** is implicitly created for `my_iterable`, assigning each extracted value to `x` until all items are processed. After the loop, `x` retains the last assigned value (**4** in this case).

#### 1.2. Modifying the Iterable Itself

```python
my_iterable = [1, 2, 3, 4]
for index, x in enumerate(my_iterable):
	my_iterable[index] += 1

print(my_iterable)
# Output: [2, 3, 4, 5]
```

This example uses `enumerate` to get both the index and value of each element, allowing you to modify the original list during iteration.

#### 1.3. Executing Code Multiple Times
```python
for x in range(5):
	print(x, end=', ') 
# Output: 0, 1, 2, 3, 4, 

for x in range(1, 10, 2):
	print(x, end=', ') 
# Output: 1, 3, 5, 7, 9, 
```

The `range` data type creates an immutable sequence of numbers, useful for controlling loop iterations. It follows the syntax: `range(start, stop, step)`, similar to list slicing.

#### **Problems (For Loop):**

1. **Sum of Even Numbers:**  Write a program that calculates the sum of all even numbers from 1 to 20 using a `for` loop.
2. **Factorial:**  Calculate the factorial of a given number using a `for` loop. (Factorial of 5 = 5x4x3x2x1)
3. **List Reversal:** Reverse a list using a `for` loop and store the reversed elements in a new list.
4. **Pattern Printing:** Print the following pattern using nested `for` loops:
   ```
   SEQUENCE_WORD
   *
   **
   ***
   ****
   *****
   SEQUENCE_WORD
   ```
5. **Vowel Counter:** Write a program that counts the number of vowels in a given string using a `for` loop. 

### **2. "While" loop**

The `while` loop repeatedly executes a block of code as long as a given condition remains True.

```python
count = 0
while count < 5:
    print(count)
    count += 1
# Output: 0 1 2 3 4 
```

`while` instructions is often used to create eternal loops, which can be interrupted with use of `break` instruction. Some examples of this may include:
1. Continuous user input:
```python
while True: 
	user_input = input("Enter a command (type 'exit' to quit): ") 
	if user_input == "exit": 
		print("Exiting program.") 
		break
	else: 
		print(f"You entered:{user_input}")
```
2. Server Listening for Connections:
```python
while True: 
	connection = server_socket.accept() 
	print(f"Connected to: {connection[1]}") 
	# Process the connection here 
	handle_connection(connection) 
	# Optionally break based on a certain condition
```
3. Automated Data Collection:
```python
while True:
	# Collect new data
	response = requests.get(api_url, params=params) 
	data = response.json()
	# Save the data locally using json
	json.dump(filename, data)
	
```
#### 2.1.  Break and continue
* **`break`:** Immediately terminates the loop, regardless of the loop's condition.
* **`continue`:**  Skips the current iteration and jumps to the next iteration of the loop.

#### **Problems (While Loop):**

1. **Guessing Game:**  Create a number guessing game.  Generate a random number between 1 and 100, and ask the user to guess the number. Provide feedback (higher or lower) after each guess. Use a `while` loop to keep the game running until the user guesses correctly.
2. **Sum Until Zero:** Write a program that continuously prompts the user to enter numbers until they enter 0. Calculate and print the sum of all entered numbers.
3. **Collecting Even Numbers:** Write a program that repeatedly asks the user to enter a number. The program should collect all the even numbers in a list and ignore the odd numbers. If the user enters `"done"`, the program should stop asking for numbers and print the list of collected even numbers.
4. **Password Check:** Create a program that continuously prompts the user to enter a password. The program should check if the password meets the following criteria:
	- At least 8 characters long
	- Contains at least one uppercase letter
	- Contains at least one lowercase letter
	- Contains at least one number
	
	If the password doesn't meet any of these criteria, inform the user which criteria were not met and prompt them to try again. The loop should break when a valid password is entered.

5. **Secret Word Game:** Create a game where the user has to guess a secret word, which is predefined in the code. The word is displayed with star '\*' characters (apple - > \*\*\*\*\*). The user can guess a single character, which will be shown if the guess is lucky (\*pp\*\*), or try to guess a whole word. Each time the user guesses incorrectly, the program should prompt them to guess again. When the user guesses the correct word or types `"quit"`, the loop should break.

6. **Fibonacci Sequence:** Print the Fibonacci sequence up to a given number using a `while` loop.

7.  **Counting Vowels:** Create a program that asks the user to enter a sentence. The program should then count the number of vowels (`a, e, i, o, u`) in the sentence. If the sentence contains any digits, the program should inform the user that digits are not allowed and prompt them to enter a new sentence. The loop should break once a valid sentence is entered and the vowel count is displayed.