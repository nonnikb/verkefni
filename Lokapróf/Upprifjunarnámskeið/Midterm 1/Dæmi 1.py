month = input("Input a month: ")
day = int(input("Input a date: "))

full_date = "{0} {1} ".format(month.capitalize(), str(day))
if full_date == "January 1":
    print("New year's day")
elif full_date == "June 17":
    print("National holiday")
elif full_date == "December 25":
    print("Christmas day")
else:
    print("Not a holiday")