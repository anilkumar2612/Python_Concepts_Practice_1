# The inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we
# derive from are called base classes. Important benefits of inheritance are code reuse and reduction of complexity of a program. The derived classes (descendants) override
# or extend the functionality of base classes (ancestors).




class Animal(object):

    def __init__(self):
        print "Animal Created"

    def Whoami(self):
        print "Animal"

    def eat(self):
        print "Eating"


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print "Dog Created"

d=Dog()

d.eat()
d.Whoami()
