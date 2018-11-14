"""Write a Python program using a for loop, that given two integers
as input, prints the greatest common divisor (gcd) of them.
GDC is the largest integer that divides each of the two integers.
for example, with the numbers 12 and 15 the output would be 3"""

a = int(input("Input first number: "))
b = int(input("Input second number: "))
gdb = 1
for i in range(1,a+1):
    if a%i==0 and b%i==0:
        gcd = i
print(gcd)
