#The difference between shallow and deep copying is only relevant for compound objects, which are objects containing other objects, like lists or class instances.
from copy import copy, deepcopy

colours1=['red','green','yellow','black']
#c2 & c1 bind to list object
colours2=colours1
#c2 is bind to new list
colours2=['voilet','brown']

print colours1
print colours2


#both bind to same list object, if list is changed using one name other will be changed
c1=['red','green','yellow','black']
c2=c1
c2[3]='blue'
print c1


#create a new object while binding to another use slice

l1=[1,1,1,1,1,1,1,1,1]
l2=l1[:]

l1[4]=4

print l1
print l2

#creting a new list from a compund list using slice, will create some side effects


