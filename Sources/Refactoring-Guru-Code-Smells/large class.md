---
type: note
status: done
tags: ['tech/python']
sources:
authors:
- "[[Refactoring Guru - Code Smells]]"

---

#🃏/semantic/code-smells #🃏/source/refactoring-guru/code-smells

Then class is wearing to many functional hats, there are few techniques to consider:
- If behaviour of the class can be split into a separate component
- if part of the behavior of the large class can be implemented in different ways or is used in rare cases 
- if it’s necessary to have a list of the operations and behaviors that the client can use.
- while splitting, it may be necessary to store copies of some data in two places and keep the data consistent
?
- [Extract Interface](https://refactoring.guru/extract-interface) 
- [Extract Subclass](https://refactoring.guru/extract-subclass) 
-  [Duplicate Observed Data](https://refactoring.guru/duplicate-observed-data)