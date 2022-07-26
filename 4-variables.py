import sys

greet = "Hello World!"

print(greet)

print(sys.getsizeof(greet))

# list in python

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print(cheese[1])
cheese[-1] = 'Red Leicester'
print(cheese) 

mytuple = 'eggs', 'bacon', 'spam', 'tea'
print(mytuple)
print(mytuple[1])
print(mytuple[-1])

myDict = {'Australia':'Cabberra','UK':'London','India':'Delhi'}
print(myDict)


print(myDict['Australia'])

myDict['Pakisthan']="Islamabad"
   
print(myDict)
