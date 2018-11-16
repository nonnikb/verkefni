size = int(input("Input size: "))
arr = []
unique_arr = []
for i in range(size):
    arr.append(int(input("Enter Value {0}: ".format(i + 1))))

for i in arr:
    found = False
    for j in unique_arr:
        if j == i:
            found = True
    if not found:
        unique_arr.append(i)

print(unique_arr)
print("The list: ",arr)

print("The list with no duplicates: ", unique_arr)
print(set(arr))







