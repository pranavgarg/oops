
Three pillars of Object Oriented Programming : Python

## ENCAPSULATION
Methods to **gate** the way the data gets stored inside the class.
 
- getter 
- setter  
- constructor

## INHERITANCE
- One class can inherit from another, in particular its methods are inherited in the child class. 
- Simply one other level of attribute lookup: _instance_ then _class_, then _inherited classes_.

Benefits
- helps in removing duplicate code by allowing use of parent/base class to have common functions
Things that can be achieved:
 1. Inherit a method: simply use the parent's class method
 2. Override : provide child's own version of method
 3. Extend : do work in addition to a parent class's method.
 4. Provide: implement a abstract method which a parent class provides

## POLYMORPHISM
- two or more classes have the same interface(i.e. the method name)
- the methods are often different but conceptually similar like `persistData` method on `floppyDisk` class and `hardDisk` class.
- allows for expressiveness design: we can say that this group of related classes implement the same action 
- **Duck Typing** refers to reading an object's attributes to decide whether it is of a proper type, rather than checking the type itself.
e.g. len function called on tuple/list/dictionary 

Examples of each of the OOP are given in this repository for quick remembrance. 
WIP
1. design patterns
2. Useful coding patterns