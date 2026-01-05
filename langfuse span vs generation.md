---
type: note
status: done
tags: []
sources:
-
-
authors:
-
---
In Langfuse terminology, both “span” and “generation” are observation types, but they serve different purposes.[(1)](https://langfuse.com/docs/observability/sdk/python/overview)

- A **Langfuse Span** is a **generic OTel span** used for non‑LLM operations.[(1)](https://langfuse.com/docs/observability/sdk/python/overview)
- A **Langfuse Generation** is a **specialized OTel span for LLM calls**, and it includes extra fields such as `model`, `model_parameters`, `usage_details` (tokens), and `cost_details`.[(1)](https://langfuse.com/docs/observability/sdk/python/overview)

The Python SDK exposes wrappers (`LangfuseSpan`, `LangfuseGeneration`) around these OTel spans so you can work with both types while still using OpenTelemetry under the hood.[(1)](https://langfuse.com/docs/observability/sdk/python/overview)