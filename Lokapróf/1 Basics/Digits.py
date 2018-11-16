"""Input a six-digit integer.
Assign first_three(int)to be the first three digits.
Assign last_two(int) to be the last two digits
Assign middle_two to me the middle two digits.
Print out three values
Hint: use quotient // and remainder
For example if the input is 123456
The first three digits: 123
The last two digits: 56
The middle two digits: 34"""

num = input("Input a six digit integer: ")
first_three = num[:3]
last_two = num[4:]
middle_two = num[3:5]

print("The integer: ", num)
print("The first three digits are: ", first_three)
print("The last two digits are: ", last_two)
print("The middle two digits are: ", middle_two)