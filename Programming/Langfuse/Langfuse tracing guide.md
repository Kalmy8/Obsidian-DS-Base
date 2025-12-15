
### CallbackHandler

LangChain / LangGraph via `CallbackHandler` (your “default tracing”) 

With the Python SDK, Langfuse integrates with LangChain using a callback handler that you attach to your chains/agents.[(1)](https://langfuse.com/docs/observability/get-started) This handler listens to LangChain events and turns them into Langfuse observations (spans, generations, etc.).[(2)](https://langfuse.com/docs/observability/sdk/python/instrumentation)[(1)](https://langfuse.com/docs/observability/get-started) A minimal setup looks like:

```python
from langfuse.langchain import CallbackHandler 
langfuse_handler = CallbackHandler()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
 
llm = ChatOpenAI(model_name="gpt-4o")
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
chain = prompt | llm
 
response = chain.invoke(
 {"topic": "cats"}, 
 config={"callbacks": [langfuse_handler]})
```

- Chains, tools, retrievers, agents, and LLM calls are mapped to Langfuse spans/generations automatically. 
- You can set `user_id`, `session_id`, `tags` per execution via `metadata` (e.g. `langfuse_user_id`, `langfuse_session_id`, `langfuse_tags`).[(3)](https://langfuse.com/integrations/frameworks/langchain)[(1)](https://langfuse.com/docs/observability/get-started)
- You can also drive trace IDs explicitly by wrapping the LangChain execution in a span with a predefined trace ID (see section 3 below).[(4)](https://langfuse.com/docs/observability/features/trace-ids-and-distributed-tracing)[(3)](https://langfuse.com/integrations/frameworks/langchain)
### `@observe` decorator (function-level tracing)  

The `@observe()` decorator is the high-level way to trace individual functions (sync or async) in your own code.[(2)](https://langfuse.com/docs/observability/sdk/python/instrumentation)[(5)](https://langfuse.com/docs/observability/sdk/python/overview)[(1)](https://langfuse.com/docs/observability/get-started) It automatically creates a Langfuse observation around the function, capturing inputs, outputs, timing, and errors.[(2)](https://langfuse.com/docs/observability/sdk/python/instrumentation)

Example:[(2)](https://langfuse.com/docs/observability/sdk/python/instrumentation)

```python
from langfuse import observe
 
@observe()
def my_data_processing_function(data, parameter):
 # ... processing logic ...
 return {"processed_data": data, "status": "ok"}
 
@observe(name="llm-call", as_type="generation")
async def my_async_llm_call(prompt_text):
 # ... async LLM call ...
 return "LLM response"
```
- By default it captures args/kwargs as `input` and the return value as `output`. 
- `name` lets you override the span/generation name; otherwise it uses the function name. 
- `as_type="generation"` makes the observation a “generation” (LLM call) instead of a generic span. 
- `capture_input` / `capture_output` can be set per decorator or globally via `LANGFUSE_OBSERVE_DECORATOR_IO_CAPTURE_ENABLED` to control IO capture (useful for large/deep objects). 
- It automatically nests calls based on OpenTelemetry context, so an `@observe`-decorated function called inside another traced block becomes a child observation.[(2)](https://langfuse.com/docs/observability/sdk/python/instrumentation)
	- But You can also override trace context when calling a decorated function, e.g. to force a specific trace ID:[(2)](https://langfuse.com/docs/observability/sdk/python/instrumentation)[(4)](https://langfuse.com/docs/observability/features/trace-ids-and-distributed-tracing)

```python
@observe()
def my_function(a, b):
 return a + b
 
# Call with a specific trace context
my_function(1, 2, langfuse_trace_id="1234567890abcdef1234567890abcdef")
```

###  “Low-level” control

Client, context managers, manual spans, trace updates

####  Context managers: 
`start_as_current_observation` (recommended low-level API)  

Context managers are the main low-level building block. They create a span or generation and set it as the current observation in the OTEL context so children nest automatically.[(2)](https://langfuse.com/docs/observability/sdk/python/instrumentation)[(1)](https://langfuse.com/docs/observability/get-started)

Example (span + nested generation):[(2)](https://langfuse.com/docs/observability/sdk/python/instrumentation)[(1)](https://langfuse.com/docs/observability/get-started)

```python
from langfuse import get_client
 
langfuse = get_client()
 
# Create a span using a context manager
with
langfuse.start_as_current_observation(as_type="span", name="process-request") as span:

 # Your processing logic here
 # ...
 
 span.update(output="Processing complete")
 
 # Create a nested generation for an LLM call
 with langfuse.start_as_current_observation(as_type="generation", name="llm-response", model="gpt-3.5-turbo") as generation:
 # Your LLM call logic here
  generation.update(output="Generated response")
 
# All spans are automatically closed when exiting their context blocks
```
- Use `.update()` on the span/generation to set `input`, `output`, `metadata`, `version`, `level`, `status_message`, `model`, `model_parameters`, `usage_details`, `cost_details`, and `prompt` for generations.[(2)](https://langfuse.com/docs/observability/sdk/python/instrumentation)
- Use `langfuse.update_current_span()` / `langfuse.update_current_generation()` if you don’t have a direct reference but are inside a traced context.[(2)](https://langfuse.com/docs/observability/sdk/python/instrumentation)

#### Manual spans & generations 
(`start_span`, `start_generation`)  
If you don’t want the span to become the current context, you can start spans manually and end them explicitly.[(2)](https://langfuse.com/docs/observability/sdk/python/instrumentation)[(1)](https://langfuse.com/docs/observability/get-started)

```python
from langfuse import get_client
 
langfuse = get_client()
 
# Create a span without a context manager
span = langfuse.start_span(name="user-request")
 
# Your processing logic here
span.update(output="Request processed")
 
# Child spans must be created using the parent span object
nested_span = span.start_span(name="nested-span")
nested_span.update(output="Nested span output")
 
# !!! Important: Manually end the span
nested_span.end()
 
# !!! Important: Manually end the parent span
span.end()
```

You can similarly create **child generations** off a parent span or generation:[(2)](https://langfuse.com/docs/observability/sdk/python/instrumentation)

```python
from langfuse import get_client
 
langfuse = get_client()
 
parent = langfuse.start_span(name="manual-parent")

child_span = parent.start_span(name="manual-child-span")
# ... work ...
child_span.end()
 
child_gen = parent.start_generation(name="manual-child-generation")
# ... work ...
child_gen.end()
 
parent.end()
```

### Creating and controlling trace-level attributes (“create/update trace”) 

There isn’t a separate “create_trace” function in the Python SDK; a Langfuse trace is created implicitly when the first observation (root span/generation) for a given OTEL trace ID is created.[(2)](https://langfuse.com/docs/observability/sdk/python/instrumentation)[(4)](https://langfuse.com/docs/observability/features/trace-ids-and-distributed-tracing)[(5)](https://langfuse.com/docs/observability/sdk/python/overview) 

**You control the trace via:**
- `update_trace()` on any span/generation object to set trace attributes like `name`, `user_id`, `session_id`, `version`, `input`, `output`.

Example of setting and overriding trace input/output:
```python
from langfuse import get_client

langfuse = get_client()

with langfuse.start_as_current_observation(as_type="span", name="complex-pipeline") as root_span:
	# Root span has its own input/output
	root_span.update(input="Step 1 data", output="Step 1 result", metadata=...)

	# But trace should have different input/output (e.g., for LLM-as-a-judge)
	root_span.update_trace(
				input={"original_query": "User's actual question"},
				output={"final_answer": "Complete response", "confidence": 0.95},
				metadata=...,  
				name=..., # Trace Name
				public=... #
			)

			# Now trace input/output are independent of root span input/output
		```

- `langfuse.update_current_trace()` to update the trace associated with the current observation.

Example of updating the current trace from within a nested function:
```python
from langfuse import observe, langfuse

@observe()
def my_internal_function():
	# Update the trace from deep within the call stack
	# without passing the trace object around
	langfuse.update_current_trace(
		user_id="user_123",
		tags=["production", "beta-feature"]
	)
```

- `propagate_attributes(...)` context manager to set attributes that automatically apply to all observations in that execution context (e.g. `user_id`, `session_id`, `version`, `tags`, `metadata`).

Example of attribute propagation and cross-service propagation:
```python
from langfuse import get_client, propagate_attributes
import requests

langfuse = get_client()

# Service A - originating service
with langfuse.start_as_current_observation(as_type="span", name="api-request"):
	with propagate_attributes(
		user_id="user_123",
		session_id="session_abc",
		as_baggage=True # Propagate via HTTP headers
	):
		# HTTP request to Service B
		response = requests.get("https://service-b.example.com/api")
		# user_id and session_id are now in HTTP headers

# Service B will automatically extract and apply these attributes
```


e) Custom / deterministic trace IDs  
To align Langfuse traces with your own IDs (e.g. messageId, correlationId), you can use deterministic trace IDs via `create_trace_id()` and then pass them into either:[(2)](https://langfuse.com/docs/observability/sdk/python/instrumentation)[(4)](https://langfuse.com/docs/observability/features/trace-ids-and-distributed-tracing)[(3)](https://langfuse.com/integrations/frameworks/langchain)

- `langfuse_trace_id` when calling an `@observe`-decorated function.[(2)](https://langfuse.com/docs/observability/sdk/python/instrumentation)[(4)](https://langfuse.com/docs/observability/features/trace-ids-and-distributed-tracing)
- `trace_context={"trace_id": ...}` when starting a span with `start_as_current_observation` (useful to wrap LangChain).[(4)](https://langfuse.com/docs/observability/features/trace-ids-and-distributed-tracing)[(3)](https://langfuse.com/integrations/frameworks/langchain)

Example with LangChain:[(3)](https://langfuse.com/integrations/frameworks/langchain)
```python
from langfuse import get_client, Langfuse
from langfuse.langchain import CallbackHandler
 
langfuse = get_client()
 
# Generate deterministic trace ID from external system
external_request_id = "req_12345"
predefined_trace_id = Langfuse.create_trace_id(seed=external_request_id)
 
langfuse_handler = CallbackHandler()
 
# Use the predefined trace ID with trace_context
with langfuse.start_as_current_observation(
 as_type="span",
 name="langchain-request",
 trace_context={"trace_id": predefined_trace_id}
) as span:
 span.update_trace(
  user_id="user_123",
  input={"person": "Ada Lovelace"}
 )
 
 # LangChain execution will be part of this trace
 response = chain.invoke(
  {"person": "Ada Lovelace"},
  config={"callbacks": [langfuse_handler]}
 )
 
 span.update_trace(output={"response": response})
 
print(f"Trace ID: {predefined_trace_id}")  # Use this for scoring later
print(f"Trace ID: {langfuse_handler.last_trace_id}")  # Care needed in concurrent environments where handler is reused
```


###  How to combine these in a “complex tracing system”

With the above primitives, a typical complex setup in Python looks like:[(2)](https://langfuse.com/docs/observability/sdk/python/instrumentation)[(3)](https://langfuse.com/integrations/frameworks/langchain)[(5)](https://langfuse.com/docs/observability/sdk/python/overview)[(1)](https://langfuse.com/docs/observability/get-started)

- Use `CallbackHandler` on LangChain/LangGraph for automatic graph-level spans and LLM generations. 
- Wrap key request handlers or pipeline stages with `start_as_current_observation(...)` spans to control trace IDs, user/session IDs, and high-level trace input/output. 
- Use `@observe` on important internal functions to get fine-grained spans nested inside those higher-level spans. 
- Use `propagate_attributes(...)` early in the request to ensure `user_id`, `session_id`, `tags`, and `metadata` are attached to everything. 
- Use `update_trace()` on a root span to set canonical trace input/output for evaluation and analytics.
