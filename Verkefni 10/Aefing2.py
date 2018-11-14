def to_list(inp):
    if ' ' in inp:
        string = inp.split(' ')
        return string
    else:
        string = inp.split(',')
        return string
# The main program starts here - DO NOT change it
the_string = input("Enter the string: ")
the_list = to_list(the_string)
print (the_list)