"""Write a program that prompts for a grade (a float).
A valid grade is between 5.0 and 10.0 (both inclusive).
The program prints out "Invalid grade!, Passing grade! or Failing grade!"
depending on the input"""

grade = float(input("Input a grade: "))

if grade <= 10.0 and grade >= 5.0:
    print("Passing grade!")
elif grade < 5.0:
    print("Failing grade!")
else:
    print("Invalid grade!")