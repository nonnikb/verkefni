"""Accept d1 and d2, the number on two dices as input.
First check to see that they are in the proper range for dice (1-6)
 if not, print the message "invalid input". Otherwise determine
 the sum. If the sum is 7 or 11, print"Winner".
 If the sum is 2, 3 or 12 print"Loser".
 Otherwise print the sum"""

d1 = int(input("Input first dice: "))
d2 = int(input("Input second dice: "))

if 1>d1 or 6<d1 or 1>d2 or 6<d2:
    print("Invalid input")
else:
    sums = d1+d2
    if sums == 7 or sums == 11:
        print("Winner")
    elif sums == 2 or sums == 3 or sums == 12:
        print("Loser")
    else:
        print(sums)
