#🃏/code_smells 


"Refused bequest": If subclass  has nothing in common with the superclass, you should ...
?
- eliminate inheritance in favor of [Replace Inheritance with Delegation](https://refactoring.guru/replace-inheritance-with-delegation).

"Refused bequest": If inheritance is appropriate, then you could ...
?
- Extract all fields and methods needed by the subclass from the parent class, put them in a new superclass, and set both classes to inherit from it ([Extract Superclass](https://refactoring.guru/extract-superclass))