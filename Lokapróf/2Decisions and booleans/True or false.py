"""In Python, an empty object (0 for int, 0.0 for float,
'' for string is considered to be False; all non-empty objects are considered to be True.
Write a program that prompts for an integer and prints out True if it is considered True,
otherwise it prints False."""

num = input("Enter a number: ")

if int(num)>0 or 0<int(num):
    print("True")
else:
    print("False")
