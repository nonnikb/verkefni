lijst = list(range(1, 101))
i = 0

while i < 100:
    print("{:>5d}".format(lijst[i]), end=" ")
    i = i+1
    if i % 10 == 0:
        print("")