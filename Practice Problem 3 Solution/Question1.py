# Write a python program that takes any string from the user and check whether it
# is a palindrome or not.

x = input("Enter any string ")

if x == x[::-1]:
    print("it is palindrome")

else:
    print("it is not a palindrome")