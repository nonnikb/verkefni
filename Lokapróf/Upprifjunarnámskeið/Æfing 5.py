size = int(input("Input size: "))
arr = []

for i in range(size):
    arr.append(int(input("Enter Value {0}: ".format(i+1))))

lowest = float("inf")

for i in range(len(arr)):
    if arr[i] < lowest:
        lowest = arr[i]

print("{0} is the lowest".format(lowest))





