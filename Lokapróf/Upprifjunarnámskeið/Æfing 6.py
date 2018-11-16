size = int(input("Input size: "))
arr = []

for i in range(size):
    arr.append(int(input("Enter Value {0}: ".format(i + 1))))

lowest = float("inf")
total = 0

for i in arr:
    total = total + i
print("{0} is the total".format(total))





