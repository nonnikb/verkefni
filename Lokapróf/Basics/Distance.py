"""You likely learned the Euclidean distance formula in high school,
the formula to find the distance between two points in a plane.
You will take the two coordinates as input and output the distance
between them.
Hint: you can use the sqrt function in the math module."""

import math

x = input("Enter x1: ")
x2 = input("Enter x2: ")
y = input("Enter y1: ")
y2 = input("Enter y2: ")

dx = (int(x2)) - int(x)
dy = int(y2) - int(y)

dist = math.sqrt(dx ** 2 + dy ** 2)

print(dist)