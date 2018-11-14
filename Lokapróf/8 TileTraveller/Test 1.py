"""dire = {}
dire['n'] = (0,1)
dire['w'] = (-1, 0)
dire['s'] = (0,-1)
dire['e'] = (1,0)"""
x, y = 1, 1
first_pos = x,y

def mov(x,y):
    if move.lower() == 'n':
        x = x+1
    elif move.lower() == 's':
        x = x-1
    elif move.lower() == 'e':
        y = y +1
    elif move.lower() == 'w':
        y = y-1
    else:
        return False
    return x, y

def pos(x,y):
    if x ==1 and y ==1:
        print("You can move n")
    if x == 2 and y ==1:
        print()



move = input("Enter move")
while pos !=3:
    print(first_pos)
    print(mov(x,y))















