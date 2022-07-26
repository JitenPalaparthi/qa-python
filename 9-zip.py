import sys

farms = ['Home Farm', 'Muckworthy',
'Scales End', 'Brown Rigg']
squirls = [42, 12, 2, 0]
rabbits = [395, 68, 57, 32]
moles = [12, 8, 0, 29]
dogs =[6,10,4,0]

for f, s, r, m, d in zip(farms, squirls, rabbits, moles,dogs):
    print('Total for', f, ':', s + r + m + d)

# int i = 200
# i>200?print("greater than"):print("not greater than")

i = 42
j = 3
print("i gt j") if i > j else print ("i lt j")
print("i gt j" if i > j else "i lt j")

# --statements if cond else --statements

a = 54
answer = a + 5 if a < 42 else 0 # This is an expression so that it returns a value
answer = a + (5 if a < 42 else 0)

a = 35 // 8 bytes
b = 36 // 8 bytes
isOK = True // 1 byte

name = "Jitendranadh"

name = name + "Palaparthi"

name = "Mr."+ name

print(a, "a is greater") if a>b else print(b,"b is greater")

c = a+b

sys.exit("Good bye")

os._exit(2)