"""Given a name in the format
lastname, firstname
where there is exactly one comma and one space, transform the name
into the format
first_inital, lastname
where
-first_initial and lastname are both capitalized
-there is exactly one period and space following the first_initial

for example, given s='ghandi, mahatma'
the output would be
M. Ghandi"""


#minn kóði
"""s = input("Enter last name, first name: ")
name = s.split(","+" ")
fname = name[1]
fletter = fname[0]
lname = name[0]
print(fletter.capitalize()+'.',lname.capitalize())"""

