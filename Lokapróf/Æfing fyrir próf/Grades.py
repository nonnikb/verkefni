counter = 1
top = []
while counter <= 5:
    x, y, n, z = input().split()
    x = int(x)
    y = int(y)
    n = int(n)
    z = int(z)
    counter = counter +1
    grade = sum([x, y, n, z])
    top.append(grade)

for i in range(len(top)):
    if top[i] == max(top):
        print(i+1, max(top))

