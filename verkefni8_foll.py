position = 1.1
victory = 3.1
LMAX = 1.0
DMAX = 1.0
RMAX = 0.1
UMAX = 0.1
travel = "(N)orth"

def west():
    if direction == LMAX :
        return direction
    move = direction + 1
    return move

def east():
    if direction == RMAX:
        return direction
    move = direction + 1
    return move

def south():
    if direction == UMAX:
        return direction
    move = direction - 0.1
    return move

def north():
    if direction == DMAX:
        return direction
    move = direction + 0.1
    return move


    #if position == 1.1:
    #   print("n - for moving up")
    #elif position == 1.2:
    #   print("n - for moving up")
    #  print("e - for moving right")

while True:
        round_pos = round(position,1)
        direction = round(position, 1)
        if direction == victory:
            print("victory")
            break
        round_pos = round(position, 1)

        if round_pos == 3.1:
            print("Victory!")
            break

        if round_pos == 1.1:
            travel = "(N)orth"
        elif round_pos == 1.2:
            travel = "(N)orth or (W)est or (S)outh."
        elif round_pos == 2.2:
            travel = "(E)ast or (S)outh."
        elif round_pos == 2.1:
            travel = "(N)orth."
        elif round_pos == 1.3:
            travel = "(E)ast or (S)outh."
        elif round_pos == 2.3:
            travel = "(E)ast or (W)est."
        elif round_pos == 3.3:
            travel = "(S)outh or (W)est."
        elif round_pos == 3.2:
            travel = "(N)orth or (S)outh."

        print("You can travel: ", travel)
        direction = input("Direction: ").lower()
        print("New position is:", str(direction))

        print("w - for moving west")
        print("e - for moving east")
        print("n - for moving north")
        print("s - for moving south")

        choice = input("Input your choice: ")

        if choice == "w":
            round_pos = west()
        elif choice == "e":
            round_pos = east()
        elif choice == "n":
            round_pos = north()
        elif choice == "s":
            round_pos = south()


        print("New position is:", str(round_pos))


