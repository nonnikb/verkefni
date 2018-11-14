"""Write a Python program using a for loop that, given a integer n
prints out all the Armstrong numbers between 0 and n.
You can assume that the maximum is 999
An Armstrong number is a number that is equal to the sum of its digits
when each digit is raised to the number of digits.
For example:
        6 is an Armstrong number because 6**1 = 6
        153 is an Armstrong number because 1**3+5**3+3**3=153"""

top_num = int(input("Input a number between 0 and 999: "))

for num in range(0,top_num):
    if (num < 10):
        order = 1
        first = num
        second = 0
        third = 0
    elif (num < 100):
        order = 2
        first = num % 10
        second = num // 10
        third = 0
    else:
        order = 3
        first = (num % 100) % 10
        second = (num % 100) // 10
        third = num // 100
        if (third**order + second**order + first**order == num):
            print(num)
