"""Write a Python program using a for loop, that given an integer as input, prints
all the integers starting from 1 up to but not including that number.
Print one number per line.
For example if the input is 4
output is 1-2-3"""

num = int(input("Input an int: "))
for i in range(1,num):
    print(i)
