"""Write a Python promgram using for loops that, given an integer n
prints all the perfect numbers from 1 to n.
A perfect number is an integer whose sum of integer divisors (excluding the number itself)
add up to the number. For example, 6 is a perfect number because
the sum of its integer divisors (1+2+3) is equal to 6."""

num = int(input("Upper number for the range: "))

for i in range(1, num+1):
    sum = 0
    for j in range(1, i+1):
        sum += j
    print(sum)