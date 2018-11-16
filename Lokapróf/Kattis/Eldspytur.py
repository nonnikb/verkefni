def multiply(a, b):
    summa = 0
    for x in range(a):
        if a % 2 == 0 and b == 1:
            print("Neibb")
            break
        elif summa > b:
            print("Neibb")
        else:
            print("Jebb")
            break
        summa += b
    return summa


a,b = input().split()
a = int(a)
b = int(b)
mult = multiply(a,b)