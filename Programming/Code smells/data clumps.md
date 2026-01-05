---
type: note
status: done
tags: ['tech/python']
sources:
- "[[Refactoring Guru - Code Smells]]"
authors:
-
---

#🃏/semantic/code-smells #🃏/source/refactoring-guru/code-smells

What are the "data clumps"? How to know if you have encountered one?
?
- Data clumps are typical lines of code which are being re-used and copypasted accross the application (like database connection-related code)
- Try mentally removing a single line from the group. If other lines do not make sense anymore - altogether they form a data clump

What are the possible treatements for "data clumps", if:
- Repeating data comprises the fields of a class
- If the same data clumps are passed in the parameters of methods
- If some of the data is passed to other methods
?
-  [Extract Class](https://refactoring.guru/extract-class) to move the fields to their own class.
- use  [Introduce Parameter Object](https://refactoring.guru/introduce-parameter-object) to set them off as a class.
- think about passing the entire data object to the method instead of just individual fields. [Preserve Whole Object](https://refactoring.guru/preserve-whole-object)
