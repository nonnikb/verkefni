"""Write a program using for loops that print out a pattern of
given *'s. Given an input n for the number of *, the program
prints 2*n-1 rows.
Example output given the input 5:
*
**
***
****
*****
****
***
**
*"""

stars = int(input("Max number of stars: "))

"""for i in range((stars)):
    for j in range(i):
        print('*', end="")
    print()

for i in range(stars, 0, -1):
    for j in range(i):
        print("*", end="")
    print()"""


for i in range(stars):
    for j in range(i):
        print('*', end="")
    print()

for i in range(stars, 0, -1):
    for j in range(i):
        print('*', end="")
    print()

