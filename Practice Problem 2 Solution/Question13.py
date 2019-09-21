# Write a Python function to print the even numbers from a given list.

lists=[]

no_of_element=int(input("ENTER NO. OF ELEMENTS= "))

for i in range(0,no_of_element):
    input_no=int(input("ENTER NO= "))
    lists.append(input_no)

print("LIST = ",lists)


def even(list):
    y= len(lists)
    print("THE EVEN NUMBERS ARE = ",end="")
    for i in range(0,y):
        x=lists[i]
        if (x%2==0):
            print(x,end=",")

even(lists)
