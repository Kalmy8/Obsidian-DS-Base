[Switch Statements](https://refactoring.guru/smells/switch-statements)

What is the rule of thumb of denying the "switch statements" code smell?
?
- You should think of polymorphism

How to treat "switch statements" code smell if:
- You do not know how to isolate the switch and put it in the right class
- If a `switch` is based on type code, such as when the program’s runtime mode is switched
- You have specified the inheritance structure
- If there aren’t too many conditions in the operator and they all call same method with different parameters
- If one of the conditional options is `null`
?
- [Extract Method](https://refactoring.guru/extract-method) and then [Move Method](https://refactoring.guru/move-method).
- [Replace Type Code with Subclasses](https://refactoring.guru/replace-type-code-with-subclasses) or [Replace Type Code with State/Strategy](https://refactoring.guru/replace-type-code-with-state-strategy).
- [Replace Conditional with Polymorphism](https://refactoring.guru/replace-conditional-with-polymorphism).
- If this case, you can break that method into multiple smaller methods with [Replace Parameter with Explicit Methods](https://refactoring.guru/replace-parameter-with-explicit-methods) and change the `switch` accordingly.
- use [Introduce Null Object](https://refactoring.guru/introduce-null-object).

 When to Ignore complex "switch statements" and leave them as is?
 ?
- When a `switch` operator performs simple actions, there’s no reason to make code changes.
- When `switch` operators are used by [[Factory pattern]]/[[Abstract Factory pattern]]