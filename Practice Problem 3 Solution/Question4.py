# Write a Python function that accepts a string and calculate the number of
# uppercase letters and lowercase letters.

stringss=input("ENTER A STRING = ")

def Check():
    upper_letters=0
    lower_letters=0
    
    for i in stringss:
        if (i.isupper()):
            upper_letters+=1
        else:

            lower_letters+=1
    print("no of upper case=",upper_letters)
    print("no of lower case=",lower_letters)
Check()