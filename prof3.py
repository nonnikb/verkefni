num = 1
arr = []
for i in range(0, 10):
    for j in range(i):
        arr.append(i)
        print(len(arr), num * sum(arr))


