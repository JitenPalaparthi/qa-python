import sys
import os
# string formatting

cur = 12000.246454

print('The currency value: {0:0.2f}'.format(cur))

var1 = 1200.3467
var2= 1200
var3= 200

print("Value1:{0:5.3f} Value2:{1} Value3:{2}".format(var1,var2,var3))

planets = {'Mercury': 57.91,
'Venus': 108.2,
'Earth': 149.597870,
'Mars': 227.94
}

for i, key in enumerate(planets.keys(), 1):
    print("{0:2d} {1:<10s} {2:5.2f} Gm".format(i, key, planets[key]))


# using interpolation 
print()
for i, key in enumerate(planets.keys(), 1):
    print(f"{i:2d} {key:<10s} {planets[key]:06.2f} Gm")

text = 'hello'
print(text.capitalize())
print(text.upper())
print('<'+text.center(12)+'>')
print('<'+text.ljust(12)+'>')
print('<'+text.rjust(12)+'>')
print('<'+text.zfill(12)+'>')

# interpolation of strings

names = ['Tom', 'Harry', 'Jane', 'Mary']
s = f"The third member is {names[3]}"

print(s)

# using the formatter
s = "The third member is {0}".format(names[3])

print(s)


names = ['Tom', 'Harry', 'Jane', 'Mary']
suffix = ['st', 'nd', 'rd', 'th']
n = 1
s = f"{str(n+1) + suffix[n]} of \
{len(names)} is {names[n]}"

text = "Remarkable bird, the Norwegian Blue"
print(text[11:14]) # between

print(text[-7:-1]) # from the end

print(text[10:]) # from 10th chars to the end
print(text[:10]) # from the 0th char to the 10th char

# split
line = 'root::0:0:superuser:/root:/bin/sh'
elems = line.split(':')

print("number of elements after split",len(elems))

for e in elems:
    print(e)

line1 = ":".join(elems)

print(line1)


## more on formatting

flt = 22/7
print("Float: {0:11.8f}, sci: {0:e}".format(flt))

first = 'Gengis'
second = 'Khan'
print("Name: {:<20s} {:<10s}".format(first, second))

fred = '{:#x}'.format(3735928559)
print(fred)

file = sys.argv[0]
perms = '0{:o}'.format((os.stat(file).st_mode) & 0o7777)
print(perms)