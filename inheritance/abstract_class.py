import abc

'''
     ABSTRACT CLASS which cannot be instantiated
'''


class SampleAbstractClass(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self, input):
        '''sets a value'''
        return

    @abc.abstractmethod
    def get_val(self):
        '''gets a value'''
        return


'''
    DERIVED CLASS
'''


class MyClass(SampleAbstractClass):
    def set_val(self,input):
        self.val = input

    def get_val(self):
        return self.val
