# Write commands to perform operations on list L[5,6,8,9,2,1] to convert it into :
#     a.[1,2,5,6,8,9]
#     b.[1,2,6,8,9]
#     c.[1,2,6,8,9,10]
#     d.[10,9,8,6,2,1]
#     e.[8]

L=[5,6,8,9,2,1]

#a
L.sort()
print(L)

#b
L.pop(2)
print(L)

#c
L.append(10)
print(L)

#d
L.reverse()
print(L)

#e
L=[L.pop(2)]
print(L)