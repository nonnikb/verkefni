"""Write a function called to_list that takes a string
as a parameter and returns a list of words in the string.
"Words" are entities that are separated by either commas, or spaces
In case the string contains neither commas nor spaces, a list should
be returned containing a single element.
Note: We are not testing for the case where both commas and spaces
are present in the string so feel free to ignore that.
The main program is given - DO NOT change it!
"""

def to_list(the_string):
    split = the_string.split(" ")
    th = []
    for x in split:
        j = x.split(",")
        for y in j:
            th.append(y)
    return th

# The main program starts here - DO NOT change it
the_string = input("Enter the string: ")
#the_list = to_list(the_string)
print (to_list(the_string))