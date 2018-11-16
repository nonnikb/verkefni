"""Series"""

n = int(input("Input initial value: "))
s = int(input("Input step: "))

total = 0
while total < 100:
    print(n)
    total = total + n
    n = n +s

print("Sum of series: ", total)