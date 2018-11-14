def populate_list(inp):
    while True:
        value = input("Enter a value to be added to list: ")
        if value.lower() == "exit":
            break
        else:
            inp.append(value)
    else:
        return value

def triple_list(inp):
    return inp*3
# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)
