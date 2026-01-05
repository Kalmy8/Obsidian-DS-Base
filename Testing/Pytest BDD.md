---
type: note
status: done
tags:
- tech/stack/pytest
- tech/testing
sources:
- '[[Test and Behavior Driven Development Course]]'
authors:
- null
---
**Codewords:** pytest-bdd, Gherkin, feature files, step definitions, scenarios, fixtures

## Theoretical Material

### Introduction to Pytest-BDD

Pytest-BDD is a plugin for the pytest testing framework that allows you to write behavior-driven tests using the Gherkin syntax. This approach helps bridge the communication gap between technical and non-technical team members by defining test cases in a human-readable format.

### Gherkin Syntax and Feature Files

Tests in pytest-bdd are written using Gherkin, a plain-text language that describes software's behavior without detailing implementation. These descriptions are stored in `.feature` files.

* **Feature:** Describes a high-level capability of the system.
* **Scenario:** A concrete example of a behavior that illustrates a feature.
* **Given:** Describes the initial context of the system.
* **When:** Describes an action or event performed by the user or system.
* **Then:** Describes an observable outcome or change in the system state.
* **And/But:** Used to extend a Given, When, or Then step.

**Example Feature File:**

```gherkin
Feature: Calculator
---
 As a user
 I want to perform basic arithmetic operations
 So that I can get accurate results

 Scenario: Add two numbers
 Given I have a calculator
 And I enter "5"
 When I press "add"
 And I enter "3"
 Then the result should be "8"

 Scenario: Subtract two numbers
 Given I have a calculator
 And I enter "10"
 When I press "subtract"
 And I enter "4"
 Then the result should be "6"
```

### Step Definitions

For each step in your `.feature` file (Given, When, Then), you need a corresponding Python function, called a "step definition," that implements the logic. Pytest-bdd uses decorators (`@given`, `@when`, `@then`) to link the Gherkin step text to your Python functions.

**Example Step Definitions:**

```python
import pytest
from pytest_bdd import scenario, given, when, then
from pathlib import Path

# Link the feature file to the test module
# When feature file is embedded, you might need to adjust how it's referenced.
# For simplicity, we assume 'calculator.feature' would be in the same logical directory
# as these step definitions if they were in separate files.
@scenario('embedded_calculator_feature', 'Add two numbers')
def test_add_two_numbers() -> None:
 """Add two numbers scenario."""
 pass

@scenario('embedded_calculator_feature', 'Subtract two numbers')
def test_subtract_two_numbers() -> None:
 """Subtract two numbers scenario."""
 pass

@given("I have a calculator")
def calculator() -> dict:
 """Initializes a calculator state."""
 return {"display": 0, "operation": None}

@given('I enter "{number}"')
def enter_number(calculator: dict, number: str) -> None:
 """Enters a number into the calculator."""
 calculator["display"] = int(number)

@when('I press "{operation_name}"')
def press_operation(calculator: dict, operation_name: str) -> None:
 """Performs an operation."""
 calculator["operation"] = operation_name

@when('I enter "{number}" again')
def enter_second_number(calculator: dict, number: str) -> None:
 """Enters the second number and performs calculation."""
 second_number = int(number)
 if calculator["operation"] == "add":
 calculator["display"] += second_number
 elif calculator["operation"] == "subtract":
 calculator["display"] -= second_number

@then('the result should be "{expected_result}"')
def check_result(calculator: dict, expected_result: str) -> None:
 """Checks the final result."""
 assert calculator["display"] == int(expected_result)
```

### Fixtures and Context Sharing

Pytest-bdd leverages pytest's powerful fixture system for managing state and sharing data between steps. A `given` step can return a value, and this value is then available as a fixture to subsequent `when` and `then` steps (or other `given` steps) that request it by name.

### Running Pytest-BDD Tests

To run your pytest-bdd tests, navigate to your project's root directory in the terminal and execute `pytest`. Pytest will automatically discover your feature files and step definitions and run the tests.

```bash
pytest -v -s # verbose output, show print statements
pytest -k "add" # run tests with "add" in their name
```

