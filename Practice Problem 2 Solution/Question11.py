# Develop a Function that takes two lists from user as parameter and compares each
# list element by element to print the items of list-2 common and uncommon in list-1

list1=[]
list2=[]

x=int(input("Enter no of elements in lists"))
for i in range(x):
    items1=int(input("Enter item"))
    list1.append(items1)
print("First list= ",list1)


for i in range(x):
    items2=int(input("Enter items"))
    list2.append(items2)
print("Second list=",list2)

def common(list1,list2):
    # for i in list1:
    #     for j in list2:
    #         if i==j:
    #             continue
    #         else:
    #             print("list are uncommon")
    #             break

    #     print("list are common")
    #     break
    if list1 == list2:
        print("list are comman ")
    else:
        print("list are uncomman")

common(list1,list2)
