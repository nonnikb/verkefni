size = int(input("Input size: "))
arr = []

for i in range(size):
    arr.append(int(input("Enter Value {0}: ".format(i+1))))

target = int(input("Input target: "))

found = 0
for a in arr:
    if target == a: # ef target er í array verður found = True
        found = found +1



if found:
    print("{0} is {1} times the list.".format(target, found))
else:
    print("{0} is {0} times in the list".format(target, found))

if target in arr: # ef target er í lista
    print("{0} is in the list.".format(target))
else:
    print("{0} is not in the list".format(target))





