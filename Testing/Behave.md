---
type: note
status: done
tags: ['tech/testing']
sources:
- "[[Test and Behavior Driven Development Course]]"
authors:
-
---

## Overview

- Is a framework for running automated tests against BDD documents written in Gherkin Syntax
- Workflow includes several steps:
	1. Prepare **feature and steps** files:![[Pasted image 20251207214513.png]]
		- .feature files are BDD docs written in Gherkin (thus containing Give, And, When, Then keywoards)
		- .**_steps.py files are python scripts, containing code emulating each of the described steps:
		- ![[Pasted image 20251207214640.png]]
		- *Note: BDD frameworks like Behave can automatically generate step definition 'skeletons' in your Python files based on the Gherkin steps you write in your .feature files. You then fill in the actual implementation logic for these steps.*
	2. **Prepare fixtures:**
		- One way would be using the **Backgrond:** keywoard which defines the initial common state for a several scenarios given next![[Pasted image 20251209235433.png]
		- Hint: you can define test data right inside feature files using vertical bars (outlining a table)![[Pasted image 20251209235537.png]]
		- This way you will be able to access that data using `context.table` variable (created automatically by Behave) ![[Pasted image 20251214231123.png]]
		- Another way would be using special methods (common to setUp/tearDown): ![[Pasted image 20251207215918.png]]
			- Behave uses statements that are really similar to those provided by [[Fixtures (Unittest and Pytest)#Unittest]] , allowing for granular environment control
			- **Example:** ![[Pasted image 20251207215952.png]]
	3. Run behave. It will automatically discover and launch all related files ![[Pasted image 20251214235504.png]]

## Feature and Step files writing tips
- Help build [[Behave]] feature files effectively
##### 1. Reduce duplication (strive for consistency)
- If you are using some step "Given: **user pressed 'Submit' button**" and it appears several times in your feature file(-s) - then you should keep that exact phrasing throughout the entire corpus
- Otherwise, if somewhere you have renamed it to - **user clicked 'Submit' button**, you will be no more able to re-use attached python code for that
##### 2. Refer to User Experience
- Imagine how the things would look like **from the user perspective**
- This means, that you do not write things like "When: User edits `customer_id`", because `customer_id` is a technical under-the-hood detail while feature files are written for your users and stakeholders as well
- **Note:** BDD is also valid for internal microservices, but in that case usually another service will act as a "user"
	- Here's an example of BDD for an internal ML microservice: 
```gherkin
Feature: LLM Microservice Response Generation
	As an API consumer
	I want the LLM microservice to generate relevant responses
	So that I can integrate it into my application

	Scenario: Successful text generation for a valid query
		Given the LLM microservice is available
		And I send a request with a valid `prompt` "What is the capital of France?"
		When the microservice processes the request
		Then I should receive a `200 OK` response
		And the `response_text` should contain "Paris"
		And the `confidence_score` should be greater than `0.8`

	Scenario: Error handling for an invalid prompt
		Given the LLM microservice is available
		When I send a request with an empty `prompt`
		Then I should receive a `400 Bad Request` response
		And the `error_message` should indicate "Prompt cannot be empty"
```
##### 3. Create a visible “signal” on the screen for [[python multiprocessing, multithreading, asyncio|I/O bound]] tasks:
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

##### 4. Use variable substitution
- General rule: we try to minimize the number of steps by generalizing them:
	- ![[Pasted image 20251215205725.png]]
	- For example, this step on the image above would match a ton of different text fields over the entire website like:
		- "I set the Name field to Max"
		- "I set the Category field to Dogs"
		- ...

##### 5. Follow the standard file structure

```
features/
│
├── a.feature # Describe features and scenarios
├── b.feature
├── environment.py # Holds before_all(), after_all()
└── steps/
 ├── common_steps.py # Variable substitution here
 ├── auth_steps.py # Domain-specific steps
 ├── api_steps.py
 └── ui_steps.py
```

- For each Gherkin statement outlined in a Feature file - we have a corresponding python test method in a corresponding step file
![[Pasted image 20251214230402.png]]

## Context Management

- ![[Pasted image 20251215204222.png]]
- Context is a data container which can hold arbitrary data and is being shared between the **features/scenarios/steps** within a test run:
	- It’s created once at the start of a test run and then **layered** as execution progresses.
##### 1️⃣ `before_all()` / `after_all()`
- **Same `context` instance**
- Exists for the **entire test run**
- Anything you attach here is visible everywhere **unless shadowed later**
``` python
def before_all(context):
	context.db = connect()
# will be accessible in all features/scenarios/steps.
```
##### 2️⃣ Feature level
When Behave enters a **feature**, it **pushes a new layer** onto `context`.
- Attributes set at feature level:
 - Visible to **all scenarios in that feature**
 - Not visible to other features
```python
def before_feature(context, feature): 
	context.api_url = "https://feature-specific"
# will be accessible in all scenarios/steps (of that feature).
```
##### 3️⃣ Scenario level (most common usage)
Each **scenario gets its own layer**.
- Attributes set here:
 - Shared **only within that scenario**
 - Automatically discarded after the scenario end
```python
def before_scenario(context, scenario): 
 context.user = create_user()
# will be accessible in all steps (of that scenario).
```
##### 4️⃣ Step level
Steps just **read/write the current context layer**.
```python
@when("I log in") 
def step_impl(context): 
	context.token = login(context.user)
```
##### Key rule: shadowing, not overwriting
- If you set the same attribute name at multiple levels:

```
before_all: 
	context.x = 1 
	
before_feature: 
	context.x = 2 
	
before_scenario: 
	context.x = 3
```
- And try to access it from multiple layers, you will get:
```
Inside the scenario :
	`context.x == 3`

After the scenario finishes:
	`context.x == 2`

After the feature finishes:
	`context.x == 1`
```

