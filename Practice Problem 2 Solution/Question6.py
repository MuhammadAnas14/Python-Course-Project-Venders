# Write a Python script to check if a given key already 
# exists in a dictionary.take dictionary as hard coded

number = {1:"Anas",6:"Talal",10:"khan"}

key=int(input("ENTER A KEY= "))

if key in number:
    print ("IT IS PRESENT IN DICTIONARY")

else:
    print("IT IS NOT PRESENT IN DICTIONARY")
