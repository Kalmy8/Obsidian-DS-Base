---
type: note
status: done
tags: [tech/python]
sources:
- "[[Refactoring Guru - Code Smells]]"
authors:
-
---

#🃏/semantic/code-smells #🃏/source/refactoring-guru/code-smells

What's the "long parameter list" codesmell about? How can it be detected?
?
- When a method has too many (3-4+) parameters

Possible treatements of "long parameter list" then:
- If some of the arguments are just results of method calls of another object
- Data received from another object is passed as parameters
- Parameters are coming from different sources
?
- [Replace Parameter with Method Call](https://refactoring.guru/replace-parameter-with-method-call)
- Pass the object itself to the method, by using  [Preserve Whole Object](https://refactoring.guru/preserve-whole-object).
- Pass them as a single parameter object via [Introduce Parameter Object](https://refactoring.guru/introduce-parameter-object).