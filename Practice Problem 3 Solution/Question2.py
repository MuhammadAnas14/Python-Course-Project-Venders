# Write a Python function that takes a list of words and returns the length of the
# longest one

words=["alpha","omega","up","down","overhead","understand","red","blue"] 

def longest(x):
    longest_Word = ""
    max_len = 0

    for word in words:

        if len(word) > max_len:
            max_len = len(word)
            longest_Word = word

    return longest_Word

z= longest(words)
print("the longest is ",z)