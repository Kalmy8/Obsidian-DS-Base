#🃏/code_smells

What are the two rules of thumb detecting if method is too long?
?
1. If your method takes more than 10 lines of code: it is very likely it shoud be split
2. If you have to comment on something inside your code: it's likely you should instead create a separate method (with explanatory naming)

What are the related refactorings to:
- Reduce length of a method body?
- What if local variables and parameters interfere with extracting a method, use ...
- If none of the previous recipes help, try moving the entire method to a separate object via ...
- If conditional operators appear: ...
- If loops appear: ...
?
-  [Extract Method](https://refactoring.guru/extract-method).
-  [Replace Temp with Query](https://refactoring.guru/replace-temp-with-query), [Introduce Parameter Object](https://refactoring.guru/introduce-parameter-object) or [Preserve Whole Object](https://refactoring.guru/preserve-whole-object).
-  [Replace Method with Method Object](https://refactoring.guru/replace-method-with-method-object).
-  [Decompose Conditional](https://refactoring.guru/decompose-conditional)
-  [Extract Method](https://refactoring.guru/extract-method).





