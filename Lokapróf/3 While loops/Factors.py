"""Write a program using a while statement, that given an int as the input
prints all the factors of that number, one in each line.
for example if the input is 15
output will be 1 - 3 - 5 - 15"""
n = int(input("input an int: "))
counter = 0

while counter <= n:
    counter = counter +1
    if n % counter == 0:
        print(counter)

