"""Write a program using for loops that, given an integer
n as input, prints all consecutive sums from 1 to n.
For example if 5 is entered, the program will print five sums of consecutive numbers
1=1
1+2=3
1+2+3=6
1+2+3+4=10
1+2+3+4+5=15
Print only the sum"""

num = int(input("Input an int: "))
i = 1
for i in range(1,num+1):
    nums = range(1, i+1)
    print(sum(nums))

