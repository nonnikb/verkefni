"""A prime number is a natural number greater than
1 that has no positive divisors other than 1 and
it self. Write a function that takes an integer
argument and returns True if the number is prime
and False otherwise. (assume that the argument is an integer
greater than 1, i.e. no need to check for erroneus input.)
Also write code that calls the function and prints out a message
saying that the given number is a prime or not."""

def is_prime(n):
    if n != 2 and n%2 ==0 or n%3==0 or n%5==0:
        return False
    else:
        return True

n = int(input("Input an integer greater than 1: "))

if is_prime(n):
    print(n, "is a prime")
else:
    print(n, "is not a prime")