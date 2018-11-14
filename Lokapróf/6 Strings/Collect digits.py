"""Given a string of any length, extract the numbers and print
them on one line without spaces.
Hint 1: start with an empty string.
Hint 2: isdigit[] is your friend.
For example, given this string.
some 1! likes 2 put 14 digits, in 3 strings
the output will be : 12143"""

my_str = "some 1! likes 2 put 14 digits, in 3 strings" #input("Input a string: ")

digit = []

for i in my_str:
    if i.isdigit():
        digit.append(i)
print(''.join(digit))