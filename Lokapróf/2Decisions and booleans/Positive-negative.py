"""Write a program that prompts for a number.
If it is negative print'Negative'.
If it is a positive number print Positive
If the input is 0 print Zero"""

num = input("Enter a number: ")

if int(num) == 0:
    print("Zero")
elif int(num) > 0:
    print("Positive")
else:
    print("Negative")
