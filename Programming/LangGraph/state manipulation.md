---
type: note
status: done
tags:
- tech/stack/langgraph
sources:
- null
- '[[LangGraph Course]]'
authors:
- null
---
[[Graph State]]
1) Если в Schema, используемой для компиляции нет ключа - его можно будет добавить, но для этого используются type hints
- При этом langgraph создает несколько "state channels",То есть мы можем иметь N независимых Schema, и писать/читать в них из произвольных нод (только если нода в аннотации типов поддерживает эту Schema)

- Это работает:
	- С простыми функциями (def/async def - без разницы, Langgraph обернет сам)
	- C простыми callable классами (с методом def __call__ или async def __call__) работает, при этом langgraph оборачивает их, делая async

- Это не работает:	
 - С RunnableCallable не работает. Только если граф скомпилирован с самым полным State
	- С ToolNode точно так же 
	- Cо сложными callable классами (с методом async def __acall__)

