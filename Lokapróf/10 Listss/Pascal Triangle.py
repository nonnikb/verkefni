"""Write a Python program that asks for the height
 of a Pasclal's triangle, then generates the triangle and
 prints it out.
 1. To generate the triangle, you start from the first row
 which is always 1, and the second row which is always 1 1
 2. After the first two rows, each row at level h is generated
 from the values at row h-1. Note that the leftmost number and
 the rightmost number in any row are always 1.
 Note that in row h, there are h numbers. """

def make_new_row(new_row):

# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)