"""King's Islands needs a program for its admission booths. When visitors to the park come up
to the booth to purchase their tickets, the worker uses this program
to figure out how much to charge them.
Each ticket cost $30
Senior citizens (age >=65) are given a 50% discount
Children under (or equal to) the age of 5 get a free ticket.
Write a program that prompts for the visitor's age and computes the ticket price (which should be a float)"""

age = int(input("Input age: "))
price = 30.0
if age >=65:
    print("$",price/2)
elif age <=5:
    print("0.0")
else:
    print("$",price)