"""Write a program using a while statement, that given a series of numbers as input,
adds them up until the input is 10 and then prints the total.
Do not add the final 10
for example, if the following numbers are input
8 - 3 - 11 - 10
the output should be 22"""

num = 0
sum = 0

while num != 10:
    num = int(input("Input a int: "))
    sum = num + sum
print(sum - 10)
