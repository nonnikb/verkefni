trip = int(input())

for a in range(0,trip):
    cnum = int(input())
    ucity = []
    for i in range(0,cnum):
        city = input()
        if city not in ucity:
            ucity.append(city)
    print(len(ucity))


