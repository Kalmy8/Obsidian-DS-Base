**Instructions:**  Answer the following questions and complete the programming tasks to the best of your ability. Show your code and output where applicable. 

### Part 1: Theory (30 points)

1. **(4 points) Explain the difference between compiled and interpreted languages.** Provide an example of a compiled language and an interpreted language.
2. **(4 points) What are the fundamental data types in Python?** Give examples of at least five different data types. 
3. **(4 points) Define mutable and immutable data types in Python.** Explain the difference between them and give two examples of each.
4. **(4 points)  What are docstrings in Python?** Explain their purpose and provide an example of how to write a docstring for a function. 
5. **(5 points)  Explain the following concepts and provide a brief code example for each:**
    * `*args`
    * `**kwargs`
    * Default parameter values in functions
    * `break` statement in loops
    * `continue` statement in loops
6. **(5 points) What is the output of the following code snippet? Explain your reasoning step-by-step.**
   ```python
   list1 = [1, 2, 3]
   list2 = list1
   list1.append(4) 
   print(list2)
   ```

### Part 2: Programming (70 points)

**Basic Problems (2 points each):**

1. Write a program that takes a user's name as input and prints a greeting message that includes their name. 
2. Calculate the area of a triangle given its base and height (obtained as user input).
3. Check if a given number is even or odd.
4. Find the largest among \<N> given numbers. All numbers come as a separate parameters to the function. 
5. Calculate the sum of all numbers in a list.

**Advanced Problems (5 points each):**

1. **Prime Number Checker:** Write a function `is_prime(num)` that takes an integer as input and returns `True` if the number is prime, and `False` otherwise. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 

2. **Palindrome Checker:** Write a function `is_palindrome(text)` that takes a string as input and returns `True` if the string is a palindrome, and `False` otherwise. A palindrome is a word, phrase, number, or other sequence of characters that reads the same backward as forward (ignoring spaces, punctuation, and capitalization). 

3. **Word Counter:** Write a program that counts the number of words in a sentence entered by the user. (Consider that words are separated by spaces).

4. **List Manipulation:** Given a list of numbers, write a program to create two new lists: one containing the even numbers from the original list and the other containing the odd numbers.

5. **Dictionary Operations:** Create a dictionary to store the names of students and their scores on a test.  
    *  Implement a function to add a new student and their score. 
    *  Implement a function to find the student with the highest score.
    *  Implement a function to calculate the average score.

## Challenging Programming Tasks

1. **Hangman Game:** Create a text-based Hangman game. The game should randomly select a word from a list, and the player must guess letters one at a time. 
2. **Text Analyzer:** Write a program that reads a text file and analyzes its content. The program should be able to:
    *  Count the number of words, sentences, and paragraphs in the text. 
    *  Determine the frequency of each word.
    *  Identify the longest and shortest words in the text.
3. **Simple Calculator:** Create a simple calculator program that can perform basic arithmetic operations (addition, subtraction, multiplication, division).  Use functions for each operation and implement error handling.
4. **To-Do List Application:** Design a simple to-do list application that allows users to add, view, mark as complete, and delete tasks. You can store tasks in a list or dictionary. 
5. **Rock, Paper, Scissors Game:** Implement a text-based Rock, Paper, Scissors game that allows a player to play against the computer.
6. **Random Password Generator:** Write a program that generates strong, random passwords that meet specific criteria (e.g., length, combination of characters). 
7. **File Encryption/Decryption:** Create a program that encrypts and decrypts files using a simple encryption algorithm.  (Note: For learning purposes, you can use a basic algorithm. Do not use this for real-world security.)
8. **Contact Book:** Build a contact book application that allows users to store and manage contact information. 

## Advanced difficulty Tasks:
### Task 1: Flexible Data Summarizer using `kwargs` and Loop Control

Design a function named `data_summarizer` that accepts a list of dictionaries. Each dictionary represents a record with various attributes (e.g., `name`, `age`, `salary`).

- The function should use `**kwargs` to allow the user to specify certain attributes to summarize (e.g., `age` and `salary`).
- If an attribute is not present in a record, it should use `continue` to skip that record.
- If all records are missing a specified attribute, it should `break` and return an error message.

```python
data = [{"name": "Alice", "age": 25, "salary": 50000},       
		{"name": "Bob", "age": None, "salary": 60000},     
		{"name": "Charlie", "age": 30},     
		{"name": "Dave", "salary": 55000} ]  
		
data_summarizer(data, age=True, salary=True) 
# Output: {'age': 55, 'salary': 165000} (skips missing values)
```


### Task 2: Custom List Filtering with Loop Control and `args`

Create a function called `filter_list` that takes a list and multiple filters as `*args`. Each filter is a lambda function that accepts an item from the list and returns `True` or `False`.

- Use nested loops to apply each filter in sequence to every item in the list.
- Allow the user to pass a `stop_on_fail` keyword argument. If `True`, `break` from the loop on the first failure.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
# Filters: even numbers, greater than 5 
filtered_numbers = filter_list(numbers, lambda x: x % 2 == 0, lambda x: x > 5, stop_on_fail=False) 
# Output: [6, 8, 10]
```

### Task 2: Complex Dictionary Updater using `kwargs` and Conditional Logic

Write a function called `update_records` that accepts a dictionary where keys are student IDs and values are student records. Each record is a dictionary with keys like `name`, `grade`, and `attendance`.

- Allow the user to specify updates for multiple records at once using `**kwargs`.
- If an update is specified for a record that doesn't exist, skip it with `continue`.
- If an update fails (e.g., if an invalid type is provided), use `break` to stop all updates and print an error.

```python
students = {1: {"name": "Alice", 
				"grade": 85, 
				"attendance": 90},     
			2: {"name": "Bob", 
				"grade": 78, 
				"attendance": 80},     
			3: {"name": "Charlie", 
				"grade": 92, 
				"attendance": 85} 
			}  
	
update_records(students, id_1={"grade": 88, "attendance": 91}, id_4={"name": "David"})  
# Output: Updates only for valid IDs and skips non-existing ones`
```