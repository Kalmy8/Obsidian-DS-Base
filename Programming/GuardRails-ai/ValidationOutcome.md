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
 **Who returns it?**
The Guard object (e.g., guard.parse(...) or guard(...)).

**What is it?**
 A comprehensive object representing the entire validation process for a single LLM output, possibly involving multiple validators, reasks, and fixes:
- **raw_llm_output:** The original LLM output
- **validated_output**: The final, possibly fixed, output
- **validation_passed:** True if all checks passed (after any fixes/reasks)
- **validation_summaries**: List of summaries for each validator (with error messages, etc.)
- **reask**: Info about reasks if used
- **error:** Top-level error message if the process failed