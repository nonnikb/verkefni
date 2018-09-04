a=[1,1,1]
n=10
print("tribonacci sequence")
print("original list"+str(a[-3:]))
print()
for i in range(n):
    sum=0
    for j in a[-3:]:
        sum+=j
    a.append(sum)
    print(a)
