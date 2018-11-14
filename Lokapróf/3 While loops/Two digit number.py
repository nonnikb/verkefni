"""Write a program using a while statement, that prints out the two digit number such
that when you square it, the resulting three digit
number has its rightmost two digits the same as the original
two digit number. That is, for a number in the form AB
AB * AB = CAB"""

"""number = 10
while number < 100:
    three_digits = number * number
    three_str = str(three_digits)
    last_two = three_str[1:]
    number_str = str(number)

    if last_two == number_str:
        print(number)

    number += 1"""

num = 10
while num < 100:
    squared = num **2
    if squared < 1000:
        rightmost_two = squared % 100
        if rightmost_two == num:
            print(num)
    num +=1