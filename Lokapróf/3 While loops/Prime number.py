"""A prime number is a whole number greater than 1 whose only factors are 1 and itself.
Write a program using a while statement, that given an int as the input, prints out "Prime"
if the int is a prime number, otherwise it prints "!Prime" """

n = int(input("Input a natural number: "))

while True:
    if n % 2 ==1:
        prime = True
        break
    elif n ==2:
        prime = True
        break
    else:
        prime = False
        break
if prime:

    print("Prime")
else:
    print("!Prime")