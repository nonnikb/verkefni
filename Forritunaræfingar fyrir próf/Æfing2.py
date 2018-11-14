size = (int(input("Enter the size of list: ")))

listi = []

while size > 0:
    value = int(input("Input a value: "))
    listi.append(value)
    size -= 1

target = input("Enter a value to search for: ")
if target in listi:
    print("Target is in list")
else:
    print("Target not in list")

