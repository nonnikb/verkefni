"""Write a function named count_case that takes a string
as an argument and returns the count of upper case
and lower case characters in the string (in that order)"""



def count_case(s):
    upper, lower = 0, 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return upper, lower

s = input("Enter a string: ")
upper, lower = count_case(s)

print("Upper case letters: ", upper)
print("Lower case letters: ", lower)
