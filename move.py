position = int(input("Input a position between 1 and 10: "))
move_rl = position
LMAX = 1
RMAX = 10

def mleft():
    if move_rl <= LMAX:
        return move_rl
    move = move_rl - 1
    return move

def mright():
    if move_rl >= RMAX:
        return move_rl
    move = move_rl + 1
    return move

while True:
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    choice = input("Input your choice: ")

    if choice == "l":
        move_rl = mleft()
    elif choice == "r":
        move_rl = mright()
    else:
        print("New position is:", str(move_rl))
        break
    print("New position is:", str(move_rl))

