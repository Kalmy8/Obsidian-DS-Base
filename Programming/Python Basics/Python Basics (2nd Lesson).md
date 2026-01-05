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

**Codewords:** Python standart IO, basic data types (int, float, str, list), their usage and methods.
### **1. Input and Output in Python**
#### **1.1 `print()` Function**

Outputs text or variables to the console.

```python
# Example 1.1.1: Displaying text
print("Hello, world!")

# Example 1.1.2: Printing variables
name = "Alice"
age = 30
print("Name:", name, "Age:", age)

# Example 1.1.3: Changing the separator
print("Hello", "world", sep=", ")

# Example 1.1.4: Changing the end character
print("Hello", end=" ")
print("world")

# Example 1.1.5: f-string for formatted output
pi = 3.14159
print(f"The value of pi is {pi:.2f}")
```

**Problems:**
- Print the values of two variables, `name` and `age`, in a sentence like `My name is [name] and I am [age] years old.`
- Print three variables, `first_name`, `middle_name`, and `last_name`, separated by a hyphen (`-`).
- Print the variable `line1` and ensure that the next print statement continues on the same line.

#### **1.2 `input()` Function**

Accepts user input from the console and creates a corresponding **string** object.

```python
# Example 1.2.1: Getting user input
name = input("Enter your name: ")
print("Hello,", name)

# Example 1.2.2: Converting input to integer
age = int(input("Enter your age: "))
print(f"You are {age} years old.")

# Example 1.2.3: Multi-line input (not commonly used, but shown for awareness)
input_lines = []
while True:
 line = input()
 if not line: # Empty line signals end of input
 break
 input_lines.append(line)
print(input_lines) #List of strings. 

```

**Problems:**

- Use the `input` function to get the user's name and print a greeting message like `Hello, [name]!`

### **2. Basic Arithmetic Operations**

#### **2.1 With Integers:**

```python
# Basic arithmetic operations
a = 10
b = 3
print("Sum:", a + b) # 13
print("Difference:", a - b) # 7
print("Product:", a * b) # 30
print("Division:", a / b) # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b) # 1
```

#### **2.2 With Floats:**

```python
# Basic float operations
x = 3.14159
y = 1.618
print("Sum:", x + y) # 4.75959
print("Difference:", x - y) # 1.52359
print("Product:", x * y) # 5.08320202
print("Division:", x / y) # 1.94121755253

# Rounding floats
z = 2.71828
rounded_z = round(z, 2)
print("Rounded to 2 decimal places:", rounded_z) # 2.72
```

**Problems:**
- Find the remainder when dividing 47 by 6.
- Calculate the result of 100 // 9.
- Round the float 3.14159 to 2 decimal places.

### **3. Strings and Basic Operations**

```python
# Indexing and slicing
message = "Hello, world!"
print("First character:", message[0]) # H
print("Substring:", message[7:12]) # world

# Stripping whitespace
whitespace_text = " Hello, world! "
print("Stripped:", whitespace_text.strip()) # Hello, world!

# Stripping specific characters
text_with_symbols = "O_OHello, world!O_O"
print("Stripped:", text_with_symbols.strip('O_O')) # Hello, world!

# Searching for a substring
sentence = "The black cat sat on the mat."
position = sentence.find("cat") # Returns the starting index of "cat"
print("Position of 'cat':", position) # 13

# Checking if a substring exists
text = "Python is fun"
print("Is 'Python' in text?", "Python" in text) # True
```

**Problems:**

- Access the third character of the string "Hello, World!".
- Extract the substring "World" from the string "Hello, World!".
- Remove leading and trailing whitespace from the string " hello " and print the result.
- Find the position of the substring "cat" in the string "The black cat sat on the mat."

### **3.1 f-strings**

**1. Floating-Point Numbers:**

```python
pi = 3.14159
print(f"Value of pi to 2 decimal places: {pi:.2f}") # 3.14
print(f"Value of pi in scientific notation: {pi:.2e}") # 3.14e+00
print(f"Value of pi in general format: {pi:.2g}") # 3.1
ratio = 0.12345
print(f"Percentage: {ratio:.2%}") # 12.35%

```

**2. Width and Alignment:** 

```python
number = 42
print(f"Width 10: {number:10}") 
print(f"Left-aligned: {number:<10}") print(f"Right-aligned: {number:>10}") print(f"Center-aligned: {number:^10}") #Output: 
# Width 10: | 42
# Left-aligned: |42 
# Right-aligned: | 42 
# Center-aligned:| 42
```

**3. String Formatting:**

```python
text = "hello world"
print(f"Truncated: {text:.5}") # hello
```

**Problems:**
- Format the float `12.345678` to 3 decimal places using an f-string.
- Use an f-string to print the variable `name` right-aligned within a width of 10 characters.
- Use an f-string to truncate the string "Hello, World!" to the first 5 characters.
- Format `0.987654321` using `:.3g`.
- Format `1234567` using `:.3e`.

### **4. Lists and Basic Operations**

```python
# Indexing and slicing
numbers = [1, 2, 3, 4, 5]
print("First element:", numbers[0]) # 1
print("Subset:", numbers[2:4]) # [3, 4]

# Appending and popping
numbers.append(6) 
print("Appended list:", numbers) # [1, 2, 3, 4, 5, 6]

numbers.insert(1, 'new_element')
print("List after insertion:", numbers) # [1, 'new_element', 2, 3, 4, 5, 6]

popped_element = numbers.pop() # Removes and returns the last element
print("Popped element:", popped_element) # 6
print("List after pop:", numbers) # [1, 'new_element', 2, 3, 4, 5]

numbers.remove("new_element")
print(numbers) #[1, 2, 3, 4, 5]

# Counting elements
new_list = [1, 1, 1, 2]
print(new_list.count(1)) # 3
```

**Problems:**

- Given the list `numbers = [10, 20, 30, 40, 50]`, retrieve the value at the second index.
- From the list `letters = ['a', 'b', 'c', 'd', 'e', 'f']`, extract a sublist containing the elements from index 2 to 4 (inclusive).
- Append the value 60 to the end of the list `numbers = [10, 20, 30, 40, 50]`.
- Remove and print the last element from the list `animals = ['cat', 'dog', 'rabbit', 'hamster']`.
- Count the number of occurrences of the letter 's' in the word 'mississippi'.

## Review Questions
Print the variable `status` followed by a message `Operation completed.` on the same line.
?
```python
status = "Success" # Example status
print(status, "Operation completed.")
# Or using f-string:
print(f"{status} Operation completed.")
```
<!--SR:!2026-10-03,365,354-->

Print ten variables, each one on the new line, using only one print statement.
?
```python
day = 22
month = "September"
print(day, "/", month)
# Or using f-string
print(f"{day}/{month}")

```
<!--SR:!2026-11-28,365,354-->

Print two variables, `city` and `temperature`, such that the output is `The temperature in [city] is [temperature] degrees.`
?
```python
city = "London"
temperature = 20
print(f"The temperature in {city} is {temperature} degrees.")
```
<!--SR:!2025-12-23,282,334-->

Use the input function to get two numbers from the user and print their sum.
?
```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Sum:", num1 + num2)
```
<!--SR:!2026-01-23,313,334-->

Round the float `5.6789` to 1 decimal place.
?
```python
num = 5.6789
rounded_num = round(num, 1)
print(rounded_num) # 5.7
```
<!--SR:!2026-11-28,365,354-->

Determine the quotient of `200 // 15`.
?
```python
quotient = 200 // 15
print(quotient) # 13
```
<!--SR:!2026-10-03,365,354-->

Compute the remainder of `123` divided by `25`.
?
```python
remainder = 123 % 25
print(remainder) # 23
```
<!--SR:!2026-11-28,365,354-->

 Check if the substring `"Python"` exists in the string `"I am learning Python programming."`
?
```python
text = "I am learning Python programming."
substring = "Python"
print(substring in text) # Output: True
```
<!--SR:!2026-11-28,365,354-->

 Strip the characters `*` from the string `***important***`.
?
```python
text = "***important***"
stripped_text = text.strip('*')
print(stripped_text) # Output: important
```
<!--SR:!2026-01-05,295,334-->

Get the substring `"Python"` from the string `"I love Python programming."`
?
```python
text = "I love Python programming."
start_index = text.find("Python")
end_index = start_index + len("Python")
substring = text[start_index:end_index]
print(substring) # Output: Python

# Or (if you know the substring is there):
text = "I love Python programming."
parts = text.split() # Creates a list of words
print(parts[2]) #Python
```
<!--SR:!2026-11-28,365,354-->

Retrieve the las character of the string `"Python"`.
?
```python
text = "Python"
last_char = text[-1]
print(last_char) # Output: n
```
<!--SR:!2026-11-28,365,354-->

Use an f-string to show `0.98765` as a percentage with 2 decimal places.
?
```python
number = 0.98765
print(f"{number:.2%}") # 98.77%
```
<!--SR:!2026-11-28,365,354-->

Format and truncate the string `"Python programming"` to display only the first 7 characters.
?
```python
text = "Python programming"
truncated_text = text[:7]
print(truncated_text) # Output: Python 
print(f"{text:.7}") # Output: Python (using f-string)
```
<!--SR:!2026-11-28,365,354-->

Print the variable `age` right-aligned within a width of 6 characters using an f-string.
?
```python
age = 30
print(f"{age:>6}") # Output: " 30"
```
<!--SR:!2026-01-22,312,334-->

Use an f-string to format `7.890123` to 3 decimal places.
?
```python
number = 7.890123
print(f"{number:.3f}") # Output: 7.890
```
<!--SR:!2026-11-28,365,334-->

Pop and print the element at index 1 from the list `cities = ['New York', 'Los Angeles', 'Chicago', 'Houston']`.
?
```python
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston']
popped_city = cities.pop(1) # pop() with index
print(popped_city) # Los Angeles
print(cities) # ['New York', 'Chicago', 'Houston']
```
<!--SR:!2026-10-03,365,354-->

Add the string `"elderberry"` to the list `fruits = ['apple', 'banana', 'cherry']`.
?
```python
fruits = ['apple', 'banana', 'cherry']
fruits.append("elderberry")
print(fruits) # ['apple', 'banana', 'cherry', 'elderberry']

```
<!--SR:!2026-11-28,365,334-->

Get the first three elements from the list `colors = ['red', 'green', 'blue', 'yellow']`.
?
```python
colors = ['red', 'green', 'blue', 'yellow']
first_three = colors[:3] # slicing
print(first_three) # ['red', 'green', 'blue']
```
<!--SR:!2026-11-28,365,334-->

Access the last element in the list `fruits = ['apple', 'banana', 'cherry', 'date']`.
?
```python
fruits = ['apple', 'banana', 'cherry', 'date']
last_fruit = fruits[-1]
print(last_fruit) # date
```
<!--SR:!2026-01-10,300,334-->

Count the number of occurrences of the letter 'o' in the word 'someverylongword'.
?
```python
word = 'someverylongword'
count = word.count('o')
print(count) # 2
```
<!--SR:!2026-11-28,365,310-->

