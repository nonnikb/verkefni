"""Write a program that keeps asking the user for new
values to be added to a list until the user enters 'exit'
After that, the program creates a new list with 3 copies
of every value in the initial list. Finally, the program
prints out all of the values in the new list.

Your program needs to be able to handle every variation of 'exit'
such as 'Exit', 'EXIT' etc."""

def populate_list(s):
    while True:
        inp = input("Enter value to be added to list:")
        if inp.lower() == "exit":
            break
        else:
            s.append(inp)
    else:
        return s

def triple_list(inp):
    return inp*3


# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)