
#The lambda operator or lambda function is a way to create small anonymous functions i.e functions without a name


celsius=[35.5, 39.2, 37.4, 27.9, 40.6]

Fahrenheit=map(lambda x:(9/5)*x+32, celsius)

print(Fahrenheit)

C=  map(lambda x:(float(5)/9)*(x-32),Fahrenheit)


print C


a=[1,2,3,4,5,6]
b=[11,12,13,14,15,16,17]
c=[-1,-2,-3,-4,-5,-6]


print a, b, c
#print map(lambda x,y:x+y,a,b)
#print map(lambda x,y,z:x+y+z,a,b,c)

