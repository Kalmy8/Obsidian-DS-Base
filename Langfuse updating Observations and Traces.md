---
type: note
status: done
tags: []
sources:
-
authors:
-
---
### Updating Observations[](https://langfuse.com/docs/observability/sdk/python/instrumentation#updating-observations)

You can update observations with new information as your code executes.

- For spans/generations created via context managers or assigned to variables: use the `.update()` method on the object.
- To update the _currently active_ observation in the context (without needing a direct reference to it): use `langfuse.update_current_span()` or `langfuse.update_current_generation()`.

**`LangfuseSpan.update()` / `LangfuseGeneration.update()` parameters:**

|Parameter|Type|Description|Applies To|
|---|---|---|---|
|`input`|`Optional[Any]`|Input data for the operation.|Both|
|`output`|`Optional[Any]`|Output data from the operation.|Both|
|`metadata`|`Optional[Any]`|Additional metadata (JSON-serializable).|Both|
|`version`|`Optional[str]`|Version identifier for the code/component.|Both|
|`level`|`Optional[SpanLevel]`|Severity: `"DEBUG"`, `"DEFAULT"`, `"WARNING"`, `"ERROR"`.|Both|
---
|`status_message`|`Optional[str]`|A message describing the status, especially for errors.|Both|
|`completion_start_time`|`Optional[datetime]`|Timestamp when the LLM started generating the completion (streaming).|Generation|
|`model`|`Optional[str]`|Name/identifier of the AI model used.|Generation|
|`model_parameters`|`Optional[Dict[str, MapValue]]`|Parameters used for the model call (e.g., temperature).|Generation|
|`usage_details`|`Optional[Dict[str, int]]`|Token usage (e.g., `{"input_tokens": 10, "output_tokens": 20}`).|Generation|
|`cost_details`|`Optional[Dict[str, float]]`|Cost information (e.g., `{"total_cost": 0.0023}`).|Generation|
|`prompt`|`Optional[PromptClient]`|Associated `PromptClient`object from Langfuse prompt management.|Generation|

```python
from langfuse import get_client 

langfuse = get_client() with langfuse.start_as_current_observation(as_type="generation", name="llm-call", model="gpt-5-mini") as gen: 

gen.update(input={"prompt": "Why is the sky blue?"}) # ... make LLM call ... 

response_text = "Rayleigh scattering..." 
gen.update( output=response_text, usage_details={"input_tokens": 5, "output_tokens": 50}, metadata={"confidence": 0.9} )
 
 # Alternatively, update the current observation in context:
 
 with langfuse.start_as_current_observation(as_type="span", name="data-processing"): 
 # ... some processing ... 
 
 langfuse.update_current_span(metadata={"step1_complete": True}) 
 
 # ... more processing ... 
 
 langfuse.update_current_span(output={"result": "final_data"})

```

### Setting Trace Attributes[](https://langfuse.com/docs/observability/sdk/python/instrumentation#setting-trace-attributes)

Trace-level attributes apply to the entire trace, not just a single observation. You can set or update these using:

- the `propagate_attributes` context manager that sets attributes on all observations inside its context and on the trace
- The `.update_trace()` method on any `LangfuseSpan` or `LangfuseGeneration` object within that trace.
- `langfuse.update_current_trace()` to update the trace associated with the currently active observation.

**Trace attribute parameters:**

| Parameter | Type | Description | Recommended Method |
| ------------ | --------------------- | ---------------------------------------------------------------- | ------------------------ |
| `name` | `Optional[str]` | Name for the trace. | `update_trace()` |
| `user_id` | `Optional[str]` | ID of the user associated with this trace. | `propagate_attributes()` |
| `session_id` | `Optional[str]` | Session identifier for grouping related traces. | `propagate_attributes()` |
| `version` | `Optional[str]` | Version of your application/service for this trace. | `propagate_attributes()` |
| `input` | `Optional[Any]` | Overall input for the entire trace. | `update_trace()` |
| `output` | `Optional[Any]` | Overall output for the entire trace. | `update_trace()` |
| `metadata` | `Optional[Any]` | Additional metadata for the trace. | `propagate_attributes()` |
| `tags` | `Optional[List[str]]` | List of tags to categorize the trace. | `propagate_attributes()` |
| `public` | `Optional[bool]` | Whether the trace should be publicly accessible (if configured). | `update_trace()` |

**Note:** For `user_id`, `session_id`, `metadata`, `version`, and `tags`, consider using `propagate_attributes()` (see below) to ensure these attributes are applied to **all spans**, not just the trace object.

In the near-term future filtering and aggregating observations by these attributes requires them to be present on all observations, and `propagate_attributes` is the future-proof solution.