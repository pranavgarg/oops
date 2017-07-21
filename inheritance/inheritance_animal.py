class Animal(object):
    def __init__(self, name):
        self.name = name
        super(Animal, self).__init__()

    def eat(self, food):
        print ("{0} eats {1}".format(self.name, food))

class Dog(Animal):
    def fetch(self, thing):
        return "{0} goes after the {1}". format(self.name, thing)


class Cat(Animal):
    def swatstring(self):
        return "{0} shreds the string". format(self.name)