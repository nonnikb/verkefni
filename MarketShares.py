"""Enter number of shares: 100
Enter price (dollars, numerator, denominator): 29 a b
Invalid price!
Enter price (dollars, numerator, denominator): 29 7 8
100 shares with market price 29 7/8 have value $2987.50
Continue: y
Enter number of shares: 1a
Invalid number!
Enter number of shares: 30
Enter price (dollars, numerator, denominator): x 1 2
Invalid price!
Enter price (dollars, numerator, denominator): 89 1 2
30 shares with market price 89 1/2 have value $2685.00
Continue: n"""




def price(shares):
    while True:
        try:
            d, n, de = input("Enter price (dollars, numerator, denominator): ").split(" ")
            dollars, numerator, denominator = float(d), float(n), float(de)
            value = dollars + (numerator/denominator)
            total = shares * value
            total = ("%.2f" % total)
            print(str(shares), "shares with the market price", d, n + "/" + de, "have value $" + str(total))
            break
        except ValueError:
            print("Invalid price")
            break


while True:
    shares = int(input("Enter number of shares: "))
    price(shares)
    con = int(input("Continue: "))
    if con == "y":
        shares = int(input("Enter number of shares: "))
        price(shares)
    else:
        break
