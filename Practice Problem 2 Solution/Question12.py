# Develop a simple calculator (using functions) that defines addition, subtraction,
# multiplication and division operation. User selects the operation as the input and
# provides the operands then output will be generated.Define a seperate funtion for each
# operation

number1=int(input("ENTER A FIRST NUMBER= "))
number2=int(input("ENTER A SECOND NUMBER= "))
operand=input("ENTER AN OPERAND(add/sub/mult/div)= ")

def add(a,b):
    print("SUM IS= ",a+b)
def subtraction(a,b):
    print("DIFFERENCE IS= ",a-b)
def multiplication(a,b):
    print("PRODUCT IS= ",a*b)
def division(a,b):
    print("DIVISION IS= ",a/b)

if operand=='add':
    add(number1,number2)
elif operand=='sub':
    subtraction(number1,number2)
elif (operand=='mult'):
    multiplication(number1,number2)
elif (operand=='div'):
    division(number1,number2)
else :
    print("invalid input")