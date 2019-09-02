list1 = ['p','r','o','b','e','o']

list2 = [1,2,3,4]

list1.insert(2,"a")
print(list1)

x = list1.pop()
print(x)
print(list1)

y = list2.pop(2)
print(y)
print(list2)

list_copy = list1.copy()
print(list_copy)

list2.remove("4")
print(list2)

list2.reverse()
print(list2)

list1.sort()
print(list1)

list2.sort()
print(list2)

