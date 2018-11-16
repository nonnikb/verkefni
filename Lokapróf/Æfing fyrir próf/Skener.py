r, c, zr, zc = [int(x) for x in input().split()]

for i in range(0,r):
    sb = ""
    for a in input():
        sb = sb + a*zc
    for x in range(zr):
        print(sb)
