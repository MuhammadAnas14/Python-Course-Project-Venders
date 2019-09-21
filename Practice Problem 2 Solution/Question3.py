# Develop a program to find out the largest integer in the list given input by user.Use
# functions and take list as a parameter

def largest(arr): 
    
    n= len(arr)
    initial = arr[0] 
  
    
    for i in range(1, n): 
        if arr[i] > initial: 
            initial = arr[i] 
    return initial
  
arr = [10, 324, 45, 90, 9808] 
n = len(arr) 
Ans = largest(arr) 
print ("Largest in given array is",Ans) 

