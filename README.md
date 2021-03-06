
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


## Python Core Syntax Resolutions [a.k.a Magic methods]
1. ```'abc' in var```   =>  ```var.__contains__('abc')```
2. ```var == 'abc'```   =>  ```var.__eq__('abc')```
3. ```var[1]``` => ```var.__getitem__(1)```
4. ```var[1:3]``` => ```var.__getslice__(1,3)```
5. ```a + v``` => ```a.__add__(b)```
6. ```len(var)``` => ```var.__len__()```
7. ```print var``` => ```var.__repr__()```


Examples of each of the OOP are given in this repository for quick remembrance. 
WIP
1. design patterns
2. Useful coding patterns

[Magic Methods Python](https://github.com/RafeKettler/magicmethods)

Some useful methods like 
- `with` helps doing the cleanup automatically when the function execution leaves the block
  e.g. 
  ```python
    class MyClass(object):
      def __enter__(self):
          print ("we have entered `with`")
          return self
      def __exit__(self, type, value, traceback):
          print ("we are leaving `with`")
      def sayhi(self):
          print ("hi instance %s"%(id(self)))
      
    with MyClass() as cc:
      cc.sayhi()
    
    print ("after the `with` block")
  ```
  
Many folks wonder whether Python has interfaces similar to like Java.
Python in general doesnt support interface as it has multiple inheritance. 
An `abstract` class is pretty much like a `interface`
```python 2.7
import abc
class InterfaceExample(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def __str__(self):
        raise NotImplementedError('users must define __str__ to use this base class')
```
Python3 
```python3
import abc
class InterfaceExample(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __str__(self):
        raise NotImplementedError('users must define __str__ to use this base class')
```
### Python classes
[New style classes in python that inherit from `object`](http://python-history.blogspot.com/2010/06/inside-story-on-new-style-classes.html)
  