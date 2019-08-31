a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-(0.5*d))/(2*a)
sol2 = (-b+(0.5*d))/(2*a)

print("The solution are a ", sol1,"and",sol2)