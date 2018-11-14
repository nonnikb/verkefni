"""BMI is a number calculated from a person's weight and height.
 The formula is: weight/height**2.
 Weight is in kilograms and height is in meters.
 Write a program that prompts for weight in kilograms and height in centimeters and
 outputs the BMI"""

height = input("Enter height in centimeters: ")
weight = input("Enter weight in kilograms: ")

bmi = float(weight)/((float(height)/100)**2)

print("BMI is: ", bmi)