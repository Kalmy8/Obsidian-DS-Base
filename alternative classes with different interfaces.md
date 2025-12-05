#🃏/code_smells 


When you have multiple classes with almost the same functionality, you should
?
- [Rename Method](https://refactoring.guru/rename-method)s to make them identical in all alternative classes.
- [Move Method](https://refactoring.guru/move-method), [Add Parameter](https://refactoring.guru/add-parameter) and [Parameterize Method](https://refactoring.guru/parameterize-method) to make the signature and implementation of methods the same
- Delete duplicated classes


If only part of the functionality of the classes is duplicated ...
?
- try using [Extract Superclass](https://refactoring.guru/extract-superclass). In this case, the existing classes will become subclasses.