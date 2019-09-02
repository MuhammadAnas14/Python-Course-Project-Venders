
ASK USER TO INPUT 1 FOR ADDITION 
AND 2 FOR SUBTRACTION

IF USER SELECTS 1 THEN TAKE 2 MORE  
INPUTS OF OPERANDS AND PRINT THE RESULT


option = input("press + for addition and - for subtraction: ")

if option == "+":
    n1 = int(input("enter n1: "))
    n2 = int(input("enter n2: "))

    print(n1+n2)

elif option == "-":
    n1 = int(input("enter n1: "))
    n2 = int(input("enter n2: "))

    print(n1-n2)

else:
    print("error. enter + or -")

