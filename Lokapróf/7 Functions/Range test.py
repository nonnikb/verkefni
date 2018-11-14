"""Write a function that takes an integer as an argument and
returns True if the number is within the range 1 to 555
(not inclusive, i.e. neither 1 nor 555 are in range.)
Also write a statement that calls the function with the given input
as an argument. """

def in_range(n):
    if 1 < n < 555:
        return True
    else:
        return False

n = int(input(("Enter a number: ")))

if in_range(n):
    print(str(n), "is in range.")
else:
    print(str(n), "is outside the range!")