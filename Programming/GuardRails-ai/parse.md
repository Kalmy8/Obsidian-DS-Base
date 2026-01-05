---
type: note
status: done
tags:
- tech/stack/guardrails-ai
sources:
- null
authors:
- null
---
# 1 Параметры:

### 1. llm_output: str



### 2. metadata: Optional[Dict]

- What it is: A dictionary containing any extra data that your validators might need to perform their checks. The content of this dictionary is entirely up to you and the requirements of your chosen validators.
- When to use it: Use it when a validator needs context beyond the llm_output string itself.
- Example 1: A validator checking for topic relevance might need the original user prompt, which you would pass as metadata={"prompt": "..."}.
- Example 2: The ArizeDatasetEmbeddings validator might need a dataset_id to compare against, which you would provide in the metadata.

---
### 3. llm_api: Optional[Callable] (re-asks only)

- What it is: An optional async function that can call a Large Language Model. This is typically the .ainvoke method of a LangChain ChatModel or a similar async client function.
- When to use it: Only use this if you want Guardrails to automatically attempt to fix a validation failure. If the initial llm_output fails validation, Guardrails will use this llm_api to "re-ask" the model for a corrected output
---
### 4. num_reasks: Optional[int] (re-asks only)

- What it is: An integer specifying the maximum number of times Guardrails should re-ask the LLM if validation continues to fail.
- When to use it: This parameter only has an effect if you have also provided an llm_api.
- num_reasks=0: (or if llm_api is not provided): If validation fails, Guardrails stops and returns the failure result immediately.
- num_reasks > 0: If validation fails, Guardrails will call the llm_api to get a new output nd validate it again, repeating this process up to num_reasks times.
---
### 5. prompt_params: Optional[Dict]  (re-asks only)

- What it is: A dictionary used to fill in any placeholder variables (e.g., ${variable_name}) in your re-ask prompt.
- When to use it: Only use this if you are performing re-asks (i.e., you've provided llm_api and num_reasks > 0) and your re-ask prompt is a template. This allows you to dynamically insert values into the prompt that is sent to the LLM during the correction attempt.

---
### 6. full_schema_reask: Optional[bool]  (re-asks only)

- What it is: A boolean that controls the behavior of re-asks when you are validating structured data (like a Pydantic model or a complex JSON object).
- When to use it: Only relevant when using Guardrails to enforce a specific output schema (e.g., with Guard.for_pydantic(...)) and performing re-asks.
- True: If a single field in the output fails, Guardrails asks the LLM to regenerate the entire JSON object. This is safer and often more reliable.
- False: Guardrails will try to ask the LLM to regenerate only the specific field that failed. This is faster but can sometimes lead to inconsistent or malformed results.

## The Flow When You Call parse()

1. Guard.parse() or AsyncGuard.parse() - Entry point
2. Guard._execute() or AsyncGuard._execute() - Internal execution orchestration
3. Runner or AsyncRunner - The actual validation orchestrator
4. Individual Validator calls - Where your custom validators get invoked
	- For Synchronous Guards:
		- **The Runner**** calls validator.validate(value, metadata)
			- validate() is the public interface that internally calls _validate()
			- You should implement _validate(), not validate()
			- If there are multiple validators, Runner iterates through all of them
	- For Async Guards (AsyncGuard):
		- **The AsyncRunner:**
			- checks if the validator has an async_validate() method
				- If it does, it calls await validator.async_validate(value, metadata)
			- If it doesn't, it falls back to running validator.validate() in a thread pool
			- If there are multiple validators, AsyncRunner iterates through all of them

