---
type: note
status: done
tags: ['tech/testing']
sources:
- "[[Test and Behavior Driven Development Course]]"
authors:
-
---

- In order to produce BDD Test Cases - one should understand and explore the problem domain, to see what actual features might be needed by the users: ![[Pasted image 20251207213412.png]]
- **Document containing all the BDD Test Cases acts as a single source of truth** and updates constantly, reflecting the relevant state of an application behavior
- **Structurally, every BDD Test Case contains of 3 parts:**
	1. **Feature:** \<title of the feature>
	2. **User Story:**
		- **As** \<role>
		- **I want** \<the desired behavior>
		- **So that** \<my motivation>
	3. **Scenarios (written in Gherkin Language):**
		1. Scenario 1: \<title of the scenario>
			- **Given**: pre-conditions (initial state of the System before the test runs)
		    - **When**: an event/user action
		    - **Then**: expected outcome
		    - **Hint**: usually we also want to use "And" and "But" keywords
		2. Scenario 2:....
	- **Example:**	 ![[Pasted image 20251207210211.png]]![[Pasted image 20251207211134.png]]
- After the document is ready, you can run some automated integration tests on it using tools like [[Behave]]


