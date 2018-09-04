n = int(input("Enter the length of the sequence: "))

num1 = 1
num2 = 2
num3 = 3

print(num1)
print(num2)
print(num3)

for i in range(0, n-3):
    sum = num1 + num2 + num3
    num1 = num2
    num2 = num3
    num3 = sum
    print(sum)
