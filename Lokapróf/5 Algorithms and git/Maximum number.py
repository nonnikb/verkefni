"""Design an algorithm that finds the maximum positive integer by a user. The user
repeatedly inputs numbers until a negative value is entered.
Make sure that you write up the algorithm before starting to code
Then implement the algorithm in Python. Put your algorithmic description in a comment"""

num_int = int(input("Input a number: "))

max = 0
num = 1

while num >=0:
    num = int(input("Input a number"))
    if num > max:
        max = num

print("The maximum is", max)