**Codewords:** Python's  `while` loop, loop control statements: `continue`, `break`.

### "While" loop
The `while` loop repeatedly executes a block of code as long as a given **boolean statement** remains True.

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

## Break and continue
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

1.  **Counting Vowels:** Create a program that asks the user to enter a sentence. The program should then count the number of vowels (`a, e, i, o, u`) in the sentence. If the sentence contains any digits, the program should inform the user that digits are not allowed and prompt them to enter a new sentence. The loop should break once a valid sentence is entered and the vowel count is displayed.