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
[[guardrails-ai]]

- Ответственна за вызов к валидирующей llm
- Инкапуслирует:
	- Model (может быть произвольной)
	- Prompt (может быть произвольным)
- Возвращает True (безопасное сообщение) или False (опасное сообщение)