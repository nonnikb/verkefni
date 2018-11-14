"""Given the input that represents a floating point number,
that is made up of digits and at least one decimal point,
 convert the input to a float and print it with the following
 specifications
 -field width of 12
 -2 decimal digits of precision
 -right justified

 for example if the input is 1234.5678
 the output will be
    1234.57
note the five spaces to the left of the digit 1"""

my_str = input("Enter a string: ")
f = float(my_str)
print("{:>12.2f}".format(f))