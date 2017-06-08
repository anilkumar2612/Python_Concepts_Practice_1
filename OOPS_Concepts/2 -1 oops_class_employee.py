

class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary



emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount


# Instead of using the normal statements to access attributes, you can use the following functions

# The getattr(obj, name[, default]) : to access the attribute of object.
#
# The hasattr(obj,name) : to check if an attribute exists or not.
#
# The setattr(obj,name,value) : to set an attribute. If attribute does not exist, then it would be created.
#
# The delattr(obj, name) : to delete an attribute.
#
# emp1.age = 7  # Add an 'age' attribute.
# emp1.age = 8  # Modify 'age' attribute.
# del emp1.age  # Delete 'age' attribute.
#
# print  emp1.age


