n = int(input("Input initial value: "))
s = int(input("Input step: "))

total = 0
print("Initial value: ", n)
print("Step: ", s)
while total < 100:
    print(n, end=" ")
    total = total +n
    n += s

print("")
print("Sum of series: ",total)