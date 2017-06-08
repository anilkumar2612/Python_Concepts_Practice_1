
# The previous objects were all built-in objects of the Python programming language. The user defined objects are created using the class keyword.
# The class is a blueprint that defines a nature of a future object. From classes we construct instances. An instance is a specific object created from a particular class.
# For example, Huck might be an instance of a Dog class.

class FirstClass(object):pass


fr=FirstClass()

print type(fr)
print type(FirstClass)


# Inside a class, we can define attributes and methods. An attribute is a characteristic of an object. This can be for example a salary of an employee.
# A method defines operations that we can perform with our objects. A method might define a cancellation of an account. Technically, attributes are variables and
# methods are functions defined inside a class.



#Object initialization

class Being(object):

    def __init__(self):
        print "Being is being initialized"

Being()


# Instance Attributes

#Attributes are characteristics of an object. Attributes are set in the __init__() method.

class Cat(object):

    def __init__(self,name):
        self.name=name

missy=Cat("Missy")
lucky=Cat("Lucky")

print missy.name
print lucky.name


# attributes_dynamic.py

class Person(object):
   pass

p = Person()
p.age = 24
p.name = "Peter"

print "{0} is {1} years old".format(p.name, p.age)



#Class object Attributes which are same for all instances of a class


class Cat(object):
    species="Mammals"

    def __init__(self,name):
        self.name=name


missy=Cat("Missy")
missy.name
print missy.__class__.species
print  type(missy).species
print  Cat.species









