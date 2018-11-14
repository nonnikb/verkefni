"""Write a program using a while statement, that given the number n as input
prints the first n odd numbers starting from 1.
For example if the input is 4
the output is : 1   3   5   7"""

num = int(input("Input an int: "))
counter = 1
num2 = num * 2

while num2 > counter:
    if counter % 2 ==1:
        print(counter)
    counter +=1
