"""Given a string named s, move the first 3 letters to the back of the string.
Print it
For example, given s = "magic tortoise"
the output is "ic tortoisemag" """

my_str = input("Enter a string: ")

print(my_str[3:]+my_str[0:3])