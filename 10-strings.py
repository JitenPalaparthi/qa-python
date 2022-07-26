from curses.ascii import isupper
from tracemalloc import start
from more_itertools import last


euro="\u20ac"

print(euro)

message = b"Hello World" # returns a string in byte array format

print(type(message))

print("Hello","World",sep="\t$\t",end="")
print("Hello","World",sep="\t$\t",end="")

print("\nnn\n\n\nnn\n\n\n\nn") # this prints 8 new lines
print(r"\nnn\n\n\nnn\n\n\n\nn") #\n is not considered as an escape sequence

name = 'jiten'' palaparthi'

print(name)

lastname="Palaparthi"

name ="Jiten" +" "+lastname # concatination

print(name)

strlist=["Hello","Jiten","How","is","todays","session"]
fullstring1=""
for s in strlist:
    fullstring1 = fullstring1+s+" "
    

print(fullstring1)
fullstring2=" " # This space is used for each string from the list concatination
fullstring2 = fullstring2.join(strlist)
print(fullstring2)

file = """C:\\QA\\Python\\PYTHB\\""" # single \ is treated as an escape char. So always give \\
file1 = r"c:\qa\Python\pythb"
print(file1)

print("convert the string to lower case",str.lower(file))

print("length of the string",len(file))

sub = "Python"
startIndex=str.find(file,sub)
endIndex = startIndex+len(sub)

substring = file[startIndex:endIndex]

print(substring)

sub = "Python"
if sub in file:
    print("Yes",sub,"is there in ",file)
else:
    print("No",sub,"is not there in ",file)

print("Number of directories in a file , including the file",file.count("\\"))

text= "HELLO WORLD"

if text.isupper():
    print("Yes",text,"is in upper case")
else:
    print("No",text,"is not in upper case")

text="Hello Jiten@"

if text.isalpha():
    print("Yes",text,"is in in alpha chars")
else:
    print("No",text,"is not in alpha char")


