size = (int(input("Enter the size of list: ")))

listi = []

while size > 0:
    value = int(input("Input a value: "))
    listi.append(value)
    size -= 1

def average(listi):
    avg = sum(listi) / len(listi)
    return avg

print(int(average(listi)))

