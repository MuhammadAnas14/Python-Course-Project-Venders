# Write a Python Function to multiply all the values in 
# a dictionary.Take Dcitionary as parameter of functions


def multiplyDict(dict):
    result = 1
    for x in dict.values():
        result = result * x
    print(result)
        
dict={"a":2,"b":6,"c":5}
multiplyDict(dict)