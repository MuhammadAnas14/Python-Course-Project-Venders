# Write a Python program to find numbers between 100 and 400 (both included)
# where each digit of a number is an even number. The numbers obtained should
# be printed in a comma-separated sequence.End result should be printed in list

result = []
for x in range(100, 401):
    s = str(x)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        result.append(s)

print(result)
