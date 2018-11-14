"""Write a program using a while statement, that given an integer as input
prints all the integers starting from 1 up to, but not including that number.
print one number per line.
For example if the input is 4
output is
1
2
3
                    """

num = int(input("Input an int: "))

counter = 1
while num > counter:
    print(counter)
    counter = counter +1