


counter = 1
while counter <=18:
    par = int(input("Par of hole: " + str(counter)+ ": " ))
    shots = int(input("Score on hole: " + str(counter) + ": "))

    if shots < (par - 3):
        print("invalid score")
    elif shots == (par - 3):
        print("albatross")
    elif shots == (par - 2):
        print("eagle")
    elif shots == (par -1):
        print("birdie")
    elif shots == par:
        print("par")
    elif shots == (par +1):
        print("bogey")
    elif shots == (par + 2):
        print("double bogey")
    elif shots == (par + 3):
        print("triple bogey")
    elif shots > (par + 3):
        print("bad hole")

counter = counter +1
