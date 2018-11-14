"""Write a function named find_min that takes two numbers
as arguments and returns the mininum of the two.
Also write a statement that calls the function using the
given input as arguments. """

first = int(input("Input first number: "))
second = int(input("Input second number: "))
#print(min(first, second))
def find_min(first, second):
    if first < second:
        return first
    else:
        return second

print("Minimum", find_min(first, second))