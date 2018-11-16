size = int(input("Input size: "))
arr = []

for i in range(size):
    arr.append(int(input("Enter Value {0}: ".format(i+1))))

if size > 0:
    highest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > highest:
            highest = arr[i]
    print("{0} is the highest".format(highest))
else:
    print("The list is empty.")





