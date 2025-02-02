#🃏
1. Write code to ask the user for their age and print "You are \[age] years old."
2. How do you print "Hello" and "World" on the same line with a space in between?
3. Define the variable `name` and say `Hello [name]!`.
4. What's wrong? `print("Hello" end=";")` (How do you fix the error?)
5. Get two numbers from the user and print their product (multiplication).
?
```python
#1
age = int(input("Enter your age: "))
print(f"You are {age} years old.") 

#2
print("Hello", "World") # Default space
# OR
print("Hello", end=" ")
print("World")

#3
name = "Bob"
print(f"Welcome, {name}!")

#4 Error in `end=`. Correct is `` (comma needed).
print("Hello", end=";")

#5 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 * num2) 
```
