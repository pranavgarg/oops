"""
Idea here is to try inheriting from a built in datatype but restrict the input to certain types for data validation
"""
import unittest

class MyDict(dict):
    def __setitem__(self, key, value):
        print ('setting the key, value pair')
        if not isinstance(value, int):
            raise "Only int values allowed"
        dict.__setitem__(self, key, value)


dd = MyDict()
dd['a'] = 5
dd['b'] = 6

assert dd.keys() == ['a','b']

dd['c'] = 'hi' #raises exception