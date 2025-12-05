#🃏/code_smells 

What is the "primitives obsession"?
?
- It's a code smell, which appeares when a programmer avoid creating separate dataclasses/type classes for storing logically-related data, and use arrays of strings/dictionaries/other primitives instead

What are the treatements, if:
- If you have a large variety of primitive fields, which can be logically grouped together
- If the values of primitive fields are used in method parameters
- When complicated data is coded in variables, use
 ?
- Move related fileds in a separate class, also try to move the behavior associated with this data too [Replace Data Value with Object](https://refactoring.guru/replace-data-value-with-object).
 - [Introduce Parameter Object](https://refactoring.guru/introduce-parameter-object) or [Preserve Whole Object](https://refactoring.guru/preserve-whole-object).
-  [Replace Type Code with Class](https://refactoring.guru/replace-type-code-with-class), [Replace Type Code with Subclasses](https://refactoring.guru/replace-type-code-with-subclasses) or [Replace Type Code with State/Strategy](https://refactoring.guru/replace-type-code-with-state-strategy).