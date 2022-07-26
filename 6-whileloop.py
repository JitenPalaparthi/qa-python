
i = 1

while i<=10:
    print(i)
    i = i+1

# even numbers

i=2

while i<=10:
    print(i)
    i= i+2

i=1
# print even numbers using another logic
while i<=10:
    if i%2!=0:
        i = i+1
        continue # continues to the next interation;skips the ongoing iteration
    print(i)
    i = i+1

while True:
    if i==101:
        break # it breaks the whole loop
    if i%2==0:
        print(i)
    i=i+1