age = 18

if age >=18:
    print("Eligible for vote in elections")
    print("Given age is ",age)
else:
    print("Not eligible for vote in elections")
    print("Given age is ",age)


num = 55
# true and true is true
# true or false is true

if num>=50 and num<100:
    print(num,"is greater than or 50 and less than 100")
elif num>=100 and num<150:
    print(num,"is greater than or 100 and less then 150")
else:
    print(num , "is either less than 50 or greater then or 150")

# List example

list1=[1,2,3,4,5,6]
list2=[1,2,3,4,5]

if list1==list2: # directly compare lists
    print("both the list are same")
else:
    print("lists are different")

## in reserve word in list
if 6 in list1:
    print("6 exists in the list")
else:
    print("6 not there in the list")

## Truth

names =["Jiten","Roy","John","Emily","Sita","Rahman","Shabnum"]
names1=[]

if names:
    print("The list is true")
else:
    print("it is false")

str =""

if str:
    print("str is not empty")
else:
    print("str is empty")

## all and any

list3=[0,1,1,2,3,4,5,6]

if all(list3):
    print("all are true")
else:
    print("all elements are not true")

list4=[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]

if any(list3):
    print("any one of the elements is true then true")
else:
    print("if none of the elements are true then false")

num1="1200"
num2 = 1201

try:
    if num1 < num2:
        print("num1 and num2 are equal")
    else:
        print("num1 and num2 are not equal")
except TypeError:
    print("Invalid types compared")
