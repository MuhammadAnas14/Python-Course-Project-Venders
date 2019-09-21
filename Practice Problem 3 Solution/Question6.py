# Write a python program to generate a ​ Fibonacci series of user specified range of
# series.

n=int(input("Enter range of series = "))

x=0
y=1
for i in range (0,n):
    print(y,end=" ")
    z=x+y
    x=y
    y=z