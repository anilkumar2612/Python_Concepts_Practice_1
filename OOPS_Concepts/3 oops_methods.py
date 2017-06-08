
# Methods are functions defined inside the body of a class. They are used to perform operations with the attributes of our objects. Methods are essential in
# the encapsulation concept of the OOP paradigm. For example, we might have a connect() method in our AccessDatabase class. We need not to be informed how exactly the
# method connect connects to the database. We only know that it is used to connect to a database. This is essential in dividing responsibilities in programming,
# especially in large applications.

#methods


class Circle(object):

    pi=3.141592

    def __init__(self,radius=1):
        self.radius=radius

    def Area(self):
        return self.radius*self.radius*Circle.pi

    def setRadius(self,radius):
        self.radius=radius

    def getRadius(self):
        return self.radius


c = Circle()

c.setRadius(5)
print c.getRadius()
print c.Area()

#unbound and unbound method calls
print "Bound and Unbound Method Calls"
class Methods(object):

    def __init__(self):
        self.name="Methods"

    def getName(self):
        return self.name


m=Methods()
print m.getName()
print Methods.getName(m)






