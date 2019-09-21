# Develop a script to generate the factorial of user defined input.

number=int(input("ENTER A NUMBER = "))

result = 1
for i in range(1,number+1):
    result= result * number
    number-=1

print("THE FACTORIAL OF A GIVEN NUMBER IS = ",result)