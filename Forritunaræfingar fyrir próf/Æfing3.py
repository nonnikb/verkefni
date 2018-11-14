size = (int(input("Enter the size of list: ")))

listi = []

while size > 0:
    value = int(input("Input a value: "))
    listi.append(value)
    size -= 1

target = int(input("Enter a value to count: "))
counter = listi.count(target)

print("{} occurs {} times in the list. ".format(target, counter))

