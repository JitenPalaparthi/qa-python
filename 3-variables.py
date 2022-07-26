a = 100.23
b = 200.45
c = a+b 
print("A+B:",c)

print(type(c))
#---
a1 ="Hello"
b1 =" World"
c1=a1+b1 # concatination
print(c1)
print(type(c1))

# --------
x1 = 0x3f # 0123456789ABCDEF
print(x1)
print(type(x1))

#--------
num = 100
pi = 3.143

r = num/pi # r is of type float so cannot perform concatinations.. Hence convert r to string
#print(type(r))
print("The value of r-->"+str(r))
# ---------------------------
num2 = "1200.12"
num3 = 800

num4 = float(num2) + num3
print(num4)