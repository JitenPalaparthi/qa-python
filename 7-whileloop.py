list=[10,20,4,56,27,56,43,98]
list.insert(2,56)

list.append(100)
print("Number of occurences",list.count(56))
print(list)
list.sort()
list.sort(reverse=True)
while list:
    print(list.pop())

list.clear()


