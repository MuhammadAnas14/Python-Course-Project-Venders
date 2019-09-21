# Develop a function that takes a tuple as parameter and sorts 
# it in reverse order.

my_tuple=(4,3,"a")

def sortReverse(my_tuple):
    new_tuple=my_tuple[::-1]
    print(new_tuple)

sortReverse(my_tuple)