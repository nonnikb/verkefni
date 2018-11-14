"""Write a Python program that reads an integer from the user and prints out the
binary equivalent value.
How do we get a binary string from an integer?
The easiest method uses integer division by 2 on successive
quotients and then collects the remainders. It is best
illustrated by an example.
"""

my_int = int(input("Give me an int >=0: "))

"""binary = []

if my_int % 2 == 0:
    binary.append(0)
elif my_int % 2 == 1:
    binary.append(1)

print(binary)"""

bstr = "{0:b}".format(my_int)

print("the binary of", my_int, "is", bstr)

