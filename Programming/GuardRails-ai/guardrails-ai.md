---
type: note
status: done
tags: []
sources:
-
authors:
-
---
[[guardrails integration]]

[[Guard class]]
[[Validator class]]
[[OnFailActions]]
[[ValidationOutcome]]

# Как происходит защита?

1. **Guard** инкапсулирует несколько **Validator** при инициализации
2. **Validator** инициализируется с помощью [[OnFailActions]] и возвращает [[ValidationResult]]
3. **Guard** для каждого из **Validator** смотрит на статус **ValidationResult** + смотрит на выбранный валидатором **OnFailAction**, а далее обрабатывает их:
	- В случае **EXCEPTION** он поднимает **ValidationError,** включая туда **FailResult** ([[ValidationResult]])
	- В остальных случаях возвращает [[ValidationOutcome]]
		- Эта штука для каждого валидатора возвращает их статусы и "валидированные" сообщения
			- "Валидированные сообщения" это либо исходное сообщение, либо исправленное 

