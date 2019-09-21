# Write a program to develop a pattern mentioned below:
# Note: user input will define the number of lines to be generated with maximum number
# of *
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

#method 1
a=int(input('Enter no of lines: '))
for i in range(0,a+1):
    print('*' * i)
for w in range(a-1,0,-1):
    print('*'* w)

#method#2
star=int(input("enter number of lines"))
for x in range(0,star):
    for i in range(0,x+1):
        print("*",end="")
    print()
for y in range(star-1,0,-1):
    for j in range(0,y):
        print("*",end="")
    print()