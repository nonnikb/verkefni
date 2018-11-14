"""Design an Algorithm that generates the first n numbers in the following sequence
1,2,3,6,11,20,37
Make sure that you write up the algorithm before you code."""

#n+an-1+an-2
n = int(input("input how many numbers: "))
an = [1,2]
counter = 1
while counter < n:
    sums = sum(an[-3:])
    an.append(sums)
    counter = counter +1
print(an[:-1])

num1 = 1
num2 = 2
num3 = 3

print(num1)
print(num2)
print(num3)

for i in range(0, n-3):
    sum = num1+num2+num3
    num1 = num2
    num2 = num3
    num3 = sum
    print(sum)