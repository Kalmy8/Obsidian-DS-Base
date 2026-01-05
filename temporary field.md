---
type: note
status: done
tags: ['tech/python']
sources:
-
authors:
-
---

#🃏/semantic/code-smells

Temporary fields get their values (and thus are needed by objects) only under certain circumstances. Outside of these circumstances, they’re empty.

Where to move temporart fields and code operating on them?
?
- Temporary fields and all code operating on them can be put in a separate class via [Extract Class](https://refactoring.guru/extract-class). 
	- In other words, you’re creating a method object, achieving the same result as if you would perform [Replace Method with Method Object](https://refactoring.guru/replace-method-with-method-object).

If conditional code was used to check if the temporary field was not-null, you should ...
?
- [Introduce Null Object](https://refactoring.guru/introduce-null-object) and integrate it in that places