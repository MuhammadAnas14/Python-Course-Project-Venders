list1 = ['p','r','o','b','e','o']

list2 = [1,2,3,4]

list1.append('a')
print(list1)

list1.append(list2)
print(list1)

list1.extend(list2)
print(list1)

print(list1.index("e"))
print(list2.index(2))



