---
type: note
status: done
tags: []
sources:
-
authors:
-
---

**Codewords:** tracing, span, trace tree, observability, correlation ID, latency, cost tracking, PII, sampling, Langfuse, OpenTelemetry, LangChain, LangGraph, instrumentation, callback, middleware, trace hierarchy, metadata, redaction

## Why Tracing for AI Agents

When building AI agents, you face unique debugging challenges:
- **Non-deterministic behavior**: Same input can produce different outputs
- **Multi-step reasoning**: Failures can occur at any step (tool call, LLM call, state transition)
- **Cost visibility**: Need to track which components consume budget
- **Production debugging**: Hard to reproduce issues without seeing the full execution path

Tracing provides a structured way to record the execution flow of your agent, making it observable and debuggable.

### Tracing vs Logging vs Metrics

- **Logging**: Text messages at specific points (e.g., "User query received")
- **Metrics**: Aggregated numbers (e.g., average latency, error rate)
- **Tracing**: Hierarchical records of operations with timing, inputs/outputs, and relationships

Tracing is superior for understanding complex, multi-step agent workflows because it shows the **relationship** between operations, not just isolated events.

```python
# Example: What tracing captures vs logging
# Logging approach (limited context):
# [2024-01-15 10:23:45] INFO: Tool 'weather_api' called
# [2024-01-15 10:23:46] INFO: LLM call completed

# Tracing approach (hierarchical context):
# Trace: user_query_12345
# ├─ Span: agent_execution (duration: 2.3s)
# │ ├─ Span: tool_call_weather (duration: 0.8s, input: "Paris", output: "22°C")
# │ └─ Span: llm_call (duration: 1.2s, model: "gpt-4", tokens: 150)
---
```

**Practice Problem: Identifying Trace Points**

Consider an AI agent that:
1. Receives a user query
2. Calls a search tool to find relevant documents
3. Calls an LLM to generate a response based on the documents
4. Calls a sentiment analysis tool to check the response tone
5. Returns the final answer

**Tasks:**
1. List all the operations you would create spans for in a trace
2. Identify which spans should be nested under which parent spans
3. What metadata would you attach to each span? (Think: inputs, outputs, timing, errors, costs)

**Expected Output:**
- A hierarchical structure showing trace → spans → nested spans
- A list of metadata fields for each span type

## Core Tracing Concepts for LLM/Agent Systems

### Traces and Spans

A **trace** represents a complete user request or workflow execution. A **span** is a single operation within that trace.

**Trace hierarchy example:**
```
Trace: "user_query_abc123"
├─ Span: agent_run (start_time, end_time, status)
│ ├─ Span: tool_call_search (input, output, duration)
│ ├─ Span: llm_call_1 (model, prompt, response, tokens, cost)
│ ├─ Span: tool_call_sentiment (input, output, duration)
│ └─ Span: llm_call_2 (model, prompt, response, tokens, cost)
```

Each span captures:
- **Timing**: Start time, end time, duration
- **Inputs/Outputs**: What went in, what came out
- **Metadata**: Model used, token counts, costs, error messages
- **Relationships**: Parent span, child spans

### Correlation IDs

A **correlation ID** (or trace ID) is a unique identifier that links all spans belonging to the same trace. This allows you to:
- Filter all operations for a single user request
- Debug failures by seeing the complete execution path
- Track requests across multiple services

```python
# Example: Using correlation IDs
import uuid

correlation_id = str(uuid.uuid4()) # e.g., "abc-123-def-456"

# All spans in this trace share the same correlation_id
trace = {
 "trace_id": correlation_id,
 "spans": [
 {"span_id": "span_1", "trace_id": correlation_id, "operation": "agent_start"},
 {"span_id": "span_2", "trace_id": correlation_id, "operation": "tool_call", "parent_id": "span_1"},
 {"span_id": "span_3", "trace_id": correlation_id, "operation": "llm_call", "parent_id": "span_1"},
 ]
}
```

### Privacy and PII Redaction

AI agents often process sensitive data (user queries, personal information). Tracing systems should support **redaction** to avoid storing PII in traces.

```python
# Example: Redacting sensitive data before tracing
def redact_pii(text: str) -> str:
 import re
 # Remove email addresses
 text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL_REDACTED]', text)
 # Remove credit card numbers (simplified)
 text = re.sub(r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b', '[CARD_REDACTED]', text)
 return text

user_query = "My email is john@example.com and my card is 1234-5678-9012-3456"
safe_query = redact_pii(user_query) # "My email is [EMAIL_REDACTED] and my card is [CARD_REDACTED]"
```

**Practice Problem: Designing a Span Hierarchy**

Design a tracing structure for a multi-tool agent that:
- Receives a user query: "What's the weather in Paris and book a flight there?"
- Calls a weather API tool
- Calls a flight booking tool
- Makes 2 LLM calls (one for planning, one for final response)

**Tasks:**
1. Draw the trace hierarchy (trace → spans → nested spans)
2. For each span, specify:
 - Span name/type
 - Parent span (if any)
 - Key metadata fields (at least 3 per span)
 - What inputs/outputs to capture
3. Identify which spans might fail independently and how you'd track errors

**Expected Output:**
- A tree diagram or nested list showing the hierarchy
- A table or list mapping each span to its metadata schema

## Tracing in Popular Agent Frameworks

### LangChain Tracing

LangChain provides **callbacks** that hook into the execution flow. You can use these to create spans automatically.

```python
from langchain.callbacks import LangfuseCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

# Initialize Langfuse callback
langfuse_handler = LangfuseCallbackHandler(
 secret_key="your-secret-key",
 public_key="your-public-key",
 host="https://cloud.langfuse.com"
)

# Create agent with tracing
llm = ChatOpenAI(temperature=0, callbacks=[langfuse_handler])
tools = [Tool(name="search", func=lambda x: f"Results for {x}")]
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

# This execution will be automatically traced
agent.run("What is the capital of France?")
```

LangChain automatically creates spans for:
- Chain execution
- Tool calls
- LLM calls
- Each step in the agent's reasoning loop

### LangGraph Tracing

LangGraph represents agents as state machines with nodes and edges. Tracing captures:
- Node executions (each node = a span)
- State transitions (edges between nodes)
- The complete state at each step

```python
from langgraph.graph import StateGraph, END
from langfuse.decorators import langfuse_context

# Example: Manual instrumentation in LangGraph
def my_node(state):
 # Start a span for this node
 with langfuse_context.trace(name="my_node"):
 # Your node logic here
 result = process_state(state)
 return {"result": result}
```

### Custom Instrumentation

For custom agents or frameworks, you manually instrument by wrapping operations:

```python
from langfuse import Langfuse

langfuse = Langfuse(
 secret_key="your-secret-key",
 public_key="your-public-key"
)

# Manual tracing
trace = langfuse.trace(name="user_query", user_id="user_123")

# Create spans
span_tool = trace.span(name="tool_call", input={"query": "Paris"})
result = call_weather_api("Paris")
span_tool.end(output={"temperature": 22})

span_llm = trace.span(name="llm_call", input={"prompt": "..."})
response = llm.generate(prompt)
span_llm.end(output={"text": response, "tokens": 150})
```

**Practice Problem: Instrumenting an Agent**

Given this pseudo-code agent:

```python
def agent(query: str):
 # Step 1: Parse query
 parsed = parse_query(query)
 
 # Step 2: Call search tool
 results = search_tool(parsed.keywords)
 
 # Step 3: Call LLM with context
 answer = llm.generate(context=results, query=query)
 
 # Step 4: Validate answer
 validated = validate_answer(answer)
 
 return validated
```

**Tasks:**
1. Mark where you would add trace/span creation calls (use comments like `# TRACE: ...`)
2. Specify what metadata you'd capture at each point
3. Show how errors would be captured in spans

**Expected Output:**
- Annotated code with trace instrumentation points
- List of metadata captured at each point

## Langfuse Basics

Langfuse is an open-source observability platform for LLM applications. It provides:
- **Traces**: Complete execution records
- **Spans**: Individual operations within traces
- **Observations**: Detailed records of LLM calls, tool calls, etc.
- **Dashboards**: Visual exploration of traces
- **Scoring**: Attach evaluation scores to traces

### Setup

```python
# Install: pip install langfuse

# Initialize (use environment variables, never hardcode secrets)
import os
from langfuse import Langfuse

langfuse = Langfuse(
 secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
 public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
 host=os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
)
```

### Basic Tracing Example

```python
from langfuse import Langfuse
import os

langfuse = Langfuse(
 secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
 public_key=os.getenv("LANGFUSE_PUBLIC_KEY")
)

# Create a trace
trace = langfuse.trace(
 name="agent_execution",
 user_id="user_123",
 metadata={"experiment": "v2", "user_tier": "premium"}
)

# Create spans for operations
span_tool = trace.span(
 name="weather_api_call",
 input={"city": "Paris"},
 metadata={"tool_version": "1.2"}
)
weather_result = {"temperature": 22, "condition": "sunny"}
span_tool.end(output=weather_result)

span_llm = trace.span(name="llm_generation")
span_llm.generation(
 model="gpt-4",
 input={"prompt": f"Weather in Paris: {weather_result}"},
 output={"text": "The weather in Paris is sunny, 22°C"},
 usage={"prompt_tokens": 50, "completion_tokens": 20}
)
span_llm.end()

# Trace is automatically finalized when it goes out of scope
```

### Langfuse Observations

Observations are detailed records within spans:
- **Generations**: LLM calls (input, output, tokens, cost)
- **Spans**: General operations (tool calls, custom logic)
- **Events**: Simple log-like entries

```python
# Using observations for detailed LLM tracking
trace = langfuse.trace(name="rag_query")

# Span for retrieval
retrieval_span = trace.span(name="document_retrieval")
docs = retrieve_documents(query)
retrieval_span.end(output={"doc_count": len(docs)})

# Generation observation for LLM call
generation = trace.generation(
 name="answer_generation",
 model="gpt-4",
 input={"query": query, "context": docs},
 output={"text": answer},
 usage={"prompt_tokens": 200, "completion_tokens": 100},
 metadata={"temperature": 0.7}
)
```

**Practice Problem: Extending Tracing with Metadata**

Extend this minimal tracing example:

```python
from langfuse import Langfuse
import os

langfuse = Langfuse(
 secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
 public_key=os.getenv("LANGFUSE_PUBLIC_KEY")
)

trace = langfuse.trace(name="simple_agent")
result = agent.run("What is 2+2?")
trace.update(output={"result": result})
```

**Tasks:**
1. Add user tier tracking (assume user_tier="premium" or "free")
2. Add experiment name tracking (assume experiment="baseline" or "experiment_v2")
3. Create nested spans for: tool calls, LLM calls, and final response formatting
4. Add error handling: if any operation fails, capture the error in the span
5. Add cost tracking: estimate token usage and cost (assume $0.03 per 1K tokens)

**Expected Output:**
- Complete code with all metadata and nested spans
- Show how errors are captured
- Show cost calculation and attachment to spans

## Advanced Langfuse Usage for Agents

### Tagging and Filtering

Tags allow you to categorize traces for easy filtering:

```python
trace = langfuse.trace(
 name="agent_run",
 tags=["production", "user_facing", "experiment_v2"]
)

# Later, filter traces by tags in Langfuse UI or API
# Filter: tags contains "experiment_v2"
```

### Querying Traces

Langfuse provides APIs to query traces programmatically:

```python
# Get traces filtered by criteria
traces = langfuse.fetch_traces(
 user_id="user_123",
 from_timestamp="2024-01-01T00:00:00Z",
 limit=100
)

# Get traces with errors
error_traces = langfuse.fetch_traces(
 tags=["production"],
 # Filter by status or error metadata
)
```

### Cost and Latency Tracking

Track costs and latency per component:

```python
trace = langfuse.trace(name="agent_execution")

# Track tool call cost
span_tool = trace.span(name="api_call")
start_time = time.time()
result = expensive_api_call()
duration = time.time() - start_time
span_tool.end(
 output=result,
 metadata={"cost_usd": 0.001, "duration_ms": duration * 1000}
)

# Track LLM cost
span_llm = trace.generation(
 name="llm_call",
 model="gpt-4",
 usage={"prompt_tokens": 1000, "completion_tokens": 500}
)
# Langfuse automatically calculates cost based on model pricing
```

### Prompt Versioning and A/B Testing

Track which prompt version was used:

```python
# Version 1
trace_v1 = langfuse.trace(
 name="agent_run",
 metadata={"prompt_version": "v1", "experiment": "baseline"}
)

# Version 2
trace_v2 = langfuse.trace(
 name="agent_run",
 metadata={"prompt_version": "v2", "experiment": "test"}
)

# Compare performance in Langfuse dashboard
```

### Connecting Tracing with Evaluation

Attach evaluation scores to traces:

```python
trace = langfuse.trace(name="rag_query")
# ... agent execution ...

# Attach evaluation score
trace.score(
 name="answer_quality",
 value=0.85,
 comment="High relevance, minor factual error"
)

trace.score(
 name="latency",
 value=1.2, # seconds
 comment="Within SLA"
)
```

**Practice Problem: Querying and Analyzing Traces**

You have traces in Langfuse for an agent that processes customer support queries. Each trace has:
- `user_id`
- `tags`: ["production", "support"]
- `metadata`: {"query_type": "billing" | "technical" | "general", "user_tier": "premium" | "free"}
- Spans with `duration_ms` and `cost_usd`

**Tasks:**
1. Write pseudo-code queries to find:
 - All traces for premium users in the last 7 days
 - Traces with latency > 2 seconds
 - Traces for "billing" queries that had errors
 - Average cost per trace by user tier
2. Design a monitoring dashboard: what 5 metrics would you track?
3. How would you use traces to debug a specific user complaint about slow responses?

**Expected Output:**
- Query specifications (pseudo-code or Langfuse API calls)
- List of 5 key metrics with rationale
- Step-by-step debugging workflow using traces

## Best Practices and Common Pitfalls

### What to Trace vs Not Trace

**Do trace:**
- User requests and agent executions
- Tool/API calls (with inputs/outputs)
- LLM calls (prompts, responses, tokens)
- Critical business logic decisions
- Errors and exceptions

**Don't trace (or sample heavily):**
- High-frequency, low-value operations (e.g., health checks)
- Operations with sensitive data (unless properly redacted)
- Internal debugging logs (use logging instead)

### Sampling Strategies

For high-traffic systems, trace everything but sample for storage:

```python
import random

def should_trace(user_id: str, query_type: str) -> bool:
 # Always trace errors
 # Sample 10% of normal traffic
 # Always trace premium users
 if user_id.startswith("premium_"):
 return True
 return random.random() < 0.1

if should_trace(user_id, query_type):
 trace = langfuse.trace(...)
```

### Handling Sensitive Data

Always redact PII before tracing:

```python
def safe_trace_input(user_input: str) -> dict:
 return {
 "query_length": len(user_input),
 "query_type": classify_query(user_input),
 # Don't store raw input if it contains PII
 "redacted_input": redact_pii(user_input)
 }

trace = langfuse.trace(
 name="agent_run",
 input=safe_trace_input(user_query) # Safe, redacted version
)
```

### Interview-Ready Tracing Strategy

When discussing tracing in interviews, cover:
1. **What you trace**: Agent executions, tool calls, LLM calls
2. **Why**: Debugging, cost tracking, performance optimization
3. **How**: Langfuse integration, correlation IDs, metadata
4. **Challenges**: Sampling, PII redaction, cost of storage
5. **Impact**: Reduced debugging time, better cost visibility, faster iteration

**Practice Problem: Critiquing a Tracing Setup**

Review this tracing implementation:

```python
from langfuse import Langfuse
import os

langfuse = Langfuse(
 secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
 public_key=os.getenv("LANGFUSE_PUBLIC_KEY")
)

def agent_with_tracing(user_query: str, user_email: str):
 # Trace everything
 trace = langfuse.trace(
 name="agent",
 input={"query": user_query, "email": user_email} # Contains PII!
 )
 
 # No error handling
 result = agent.run(user_query)
 
 # No metadata, no spans
 trace.update(output={"result": result})
 return result
```

**Tasks:**
1. Identify at least 5 issues with this implementation
2. Rewrite it following best practices:
 - Proper PII handling
 - Error handling in spans
 - Nested spans for operations
 - Useful metadata
 - Sampling consideration
3. Add cost tracking for LLM calls

**Expected Output:**
- List of issues
- Improved implementation with all best practices applied

**Key Questions:**

1. What is the difference between a trace and a span?
?
- A **trace** represents a complete user request or workflow execution (the entire journey)
- A **span** is a single operation within that trace (e.g., one tool call, one LLM call)
- Traces contain multiple spans arranged in a hierarchy (parent-child relationships)

2. When should you use tracing instead of logging?
?
- Use tracing for complex, multi-step workflows where you need to understand relationships between operations
- Use tracing when you need to debug failures across multiple components (agent → tool → LLM)
- Use logging for simple, isolated events that don't need hierarchical context
- Tracing is better for production debugging of non-deterministic AI systems

3. What is a correlation ID and why is it important?
?
- A correlation ID (trace ID) is a unique identifier that links all spans belonging to the same trace
- It allows you to filter and view all operations for a single user request
- Essential for debugging: you can see the complete execution path from start to finish
- Enables tracking requests across multiple services or components

4. How does Langfuse differ from building your own tracing system?
?
- Langfuse provides:
 - Pre-built dashboards and UI for exploring traces
 - Automatic cost calculation for LLM calls
 - Integration with popular frameworks (LangChain, LangGraph)
 - Built-in support for evaluation scores and A/B testing
- Building your own requires implementing storage, querying, visualization, and integrations from scratch

5. How do you instrument a multi-step agent with tracing?
?
- Create a top-level trace for the agent execution
- Create nested spans for each major operation (tool calls, LLM calls, state transitions)
- Use parent-child relationships to show the execution hierarchy
- Capture inputs, outputs, timing, and errors at each span level
- Use correlation IDs to link all spans to the same trace

6. What metadata should you capture in spans for LLM calls?
?
- Model name and version
- Input prompt and output response
- Token usage (prompt tokens, completion tokens, total)
- Cost (calculated or estimated)
- Temperature and other generation parameters
- Latency/duration
- Error messages if the call failed

7. How do you handle PII (Personally Identifiable Information) in traces?
?
- Redact sensitive data before storing in traces (emails, credit cards, SSNs, etc.)
- Use regex patterns or dedicated libraries to identify and mask PII
- Store redacted versions in traces, keep original data separate if needed
- Consider not tracing operations that handle highly sensitive data
- Use environment-specific redaction rules (stricter in production)

8. What is sampling and when should you use it?
?
- Sampling means only tracing a percentage of requests (e.g., 10% of traffic)
- Use sampling for high-traffic systems to reduce storage costs
- Always trace errors and failures (100% sampling for errors)
- Consider always tracing premium users or critical workflows
- Balance between observability needs and storage costs

9. How can tracing help with cost optimization?
?
- Track costs per component (which tool calls or LLM calls are expensive)
- Identify high-cost traces and optimize those workflows
- Compare costs across different prompt versions or model choices
- Set up alerts for unexpectedly high costs
- Use cost data to make informed decisions about model selection

10. How do you debug a failing agent using traces?
?
- Find the trace for the failing request using correlation ID or user ID
- Examine the trace hierarchy to see where it failed
- Check span metadata for error messages and stack traces
- Compare with successful traces to identify differences
- Look at timing data to see if failures correlate with latency spikes
- Use trace filtering to find patterns (e.g., "all traces that failed at tool X")

11. What is the relationship between tracing and evaluation?
?
- Traces capture execution data (what happened)
- Evaluation scores measure quality (how good was the result)
- You can attach evaluation scores to traces in Langfuse
- Traces can be used to build evaluation datasets (harvest real user queries)
- The combination enables: observe → evaluate → improve → deploy → observe (feedback loop)

12. How do you integrate tracing with LangChain?
?
- Use LangfuseCallbackHandler as a callback in LangChain
- Pass the callback handler to LLM, chains, or agents during initialization
- LangChain automatically creates spans for chains, tools, and LLM calls
- No manual instrumentation needed for standard LangChain components

13. What are common pitfalls when implementing tracing?
?
- Tracing everything (too expensive, use sampling)
- Storing PII without redaction (privacy/security risk)
- Not capturing errors properly (missing failure context)
- Creating too many small spans (overhead, hard to navigate)
- Not using correlation IDs (can't link related operations)
- Ignoring cost implications of storing all traces

14. How would you explain your tracing strategy in a job interview?
?
- **What**: Trace agent executions, tool calls, LLM calls with hierarchical spans
- **Why**: Debug non-deterministic failures, track costs, optimize performance
- **How**: Langfuse integration, correlation IDs, metadata capture, PII redaction
- **Challenges**: Sampling strategy, storage costs, sensitive data handling
- **Impact**: Reduced debugging time from hours to minutes, 30% cost reduction through visibility

