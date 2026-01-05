---
type: note
status: done
tags:
- tech/python
- tech/stack/pandas
- tech/stack/pytest
sources:
- null
- '[[Pandas Basics Course]]'
authors:
- null
---
## Overview

- Is a framework for running automated tests against BDD documents written in Gherkin Syntax, integrated with the Pytest testing framework.
- Allows for automated test/technical documents generation right from the feature files.
- Workflow includes several steps:
	1. Prepare **feature and step definition** files:
		- `.feature` files are BDD docs written in Gherkin (thus containing Given, And, When, Then keywords).
		- Step definitions are Python functions, usually located in `steps/` directories or `conftest.py`, decorated with `@scenario`, `@given`, `@when`, `@then` from `pytest_bdd`.
---
 ```python
 # example_steps.py
 from pytest_bdd import scenario, given, when, then, parsers

 @scenario('example.feature', 'Successful text generation for a given prompt')
 def test_text_generation():
 pass

 @given("the LLM microservice is running")
 def llm_service_running():
 # Setup for the LLM service
 pass

 @when(parsers.parse('I send a request with prompt "{prompt}"'))
 def send_request(prompt):
 # Logic to send request to LLM with the given prompt
 pass

 @then("I should receive a response with a generated text")
 def check_generated_text():
 # Assert that a response with generated text is received
 pass

 @then(parsers.parse('the generated text should contain "{expected_text}"'))
 def check_text_content(expected_text):
 # Assert that the generated text contains the expected_text
 pass
 ```
	2. **Prepare fixtures:**
		- In `pytest-bdd`, you use standard Pytest fixtures (defined in `conftest.py` or other step files) to set up common state or inject dependencies.
		- The `Background:` keyword in Gherkin can be mapped to Pytest fixtures that are automatically run before scenarios.
 - You can define test data right inside feature files using vertical bars (outlining a table) with `Examples:` keyword.
 - This data is accessed in step definitions as function arguments, which `pytest-bdd` automatically provides when used with `scenario` outlines.
 ```gherkin
 # example.feature
 Feature: Calculator

 Scenario Outline: Adding two numbers
 Given I have a calculator
 When I add <a> and <b>
 Then the result should be <sum>

 Examples:
 | a | b | sum |
 | 1 | 2 | 3 |
 | 5 | 5 | 10 |
 ```
 ```python
 # calculator_steps.py
 from pytest_bdd import scenario, given, when, then, parsers
 import pytest

 @scenario('calculator.feature', 'Adding two numbers')
 def test_add_numbers():
 pass

 @pytest.fixture
 def calculator():
 class Calculator:
 def add(self, a, b):
 return a + b
 return Calculator()

 @given("I have a calculator")
 def have_calculator(calculator):
 return calculator

 @when(parsers.parse("I add {a:d} and {b:d}"))
 def add_numbers(calculator, a, b):
 return calculator.add(a, b)

 @then(parsers.parse("the result should be {sum:d}"))
 def check_sum(add_numbers, sum):
 assert add_numbers == sum
 ```
	3. Run Pytest. It will automatically discover and launch all related files.
 ```bash
 pytest
 ```

## Feature and Step files writing tips
- Help build [[Pytest-BDD]] feature files effectively
- Principles:
	1. Reduce duplication (strive for consistency)
		- If you are using some step "Given: **user pressed 'Submit' button**" and it appears several times in your feature file(-s) - then you should keep that exact phrasing throughout the entire corpus.
		- Otherwise, if somewhere you have renamed it to - **user clicked 'Submit' button**, `pytest-bdd` will treat it as a new step, and you will need to implement a new corresponding python code for that.
	2. Refer to **User Experience**
		- Imagine how the things would look like **from the user perspective**.
		- This means, that you do not write things like "When: User edits `customer_id`", because `customer_id` is a technical under-the-hood detail while feature files are written for your users and stakeholders as well.
	3. Create a visible “signal” on the screen for [[python multiprocessing, multithreading, asyncio|I/O bound]] tasks:
		- **Bad example:**
			- Given I am on the Pet Shop search page
			- When I click the "Search" button
			- Then I should see the search results
		- **Good example:**
			- Given I am on the Pet Shop search page
			- When I click the "Search" button
			- Then I should see the status "Searching..."
			- And I wait until the status changes to "Done"
			- And I should see the search results
	 - With this in place, your automated tests can:
			- Click the button
			- **Wait until that status changes to a known “response complete” state**
			- Only then check results
		- This makes tests stable because they’re synchronized with the actual response instead of arbitrary waits (`sleep(2)` etc).
- For each Gherkin statement outlined in a Feature file - we have a corresponding python test method in a corresponding step file.
