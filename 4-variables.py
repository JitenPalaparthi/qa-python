import sys

greet = "Hello World!"

print(greet)

print(sys.getsizeof(greet))

# list in python

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print(cheese[0],cheese[1],cheese[2])
cheese[-1] = 'Red Leicester'
print(cheese) 

mytuple = 'eggs', 'bacon', 'spam', 'tea'
person ='Jiten',38,"Master of Computer Applications"
print(person)
print(mytuple[1])
print(mytuple[-1])

myDict = {'Australia':'Canberra','UK':'London','India':'Delhi'}
print(myDict)


print(myDict['Australia'])

myDict['Pakisthan']="Islamabad"
   
print(myDict)
