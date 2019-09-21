# Write a Python program to sum all the items in a list.First take no of element and
# number as an input from the user and insert it into list

list_of_numbers=[]

no_of_elements=int(input("ENTER NUMBER OF ELEMENTS= "))

for i in range(0,no_of_elements):
    input_number = int(input("ENTER NUMBER= "))
    
    list_of_numbers.append(input_number)
    
print(list_of_numbers) 

sum = 0
for j in list_of_numbers:
    sum = sum + j #i is used as index number
print("SUM = ",sum)