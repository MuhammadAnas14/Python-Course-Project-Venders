# def add(*args):
#     print(args)
#     result = sum(args)
#     print(result)

# add(5,6,4,7)

def add(*args):
    print(args)
    sum(args)

add(4,2,7,1,9)

def add1(**kwargs):
    print(kwargs)

add1(name = "anas",city = "lahore", rollno ="94")


def add2(*x,**y):
    print(x)
    print(y)

add2(1,5,2,6,7,"a",name = "Anas",city = "karachi",year="second")







