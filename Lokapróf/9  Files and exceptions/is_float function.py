"""Write a function named is_float(s) that takes one argument that is a string.
It returns True if string s represets a floating point value and returns
False otherwise. You are required to use try-except. The basic concept is to
try to convert string s to a float and if it succeeds, return True, but if it
fails (that is, an exception is raised) return False. Nota that float()
raises a ValueError exception"""

def is_float(s):
    try:
        if float(s):
            return True
        else:
            return False
    except ValueError:
        return False

s = input("Input a string")
print(is_float(s))