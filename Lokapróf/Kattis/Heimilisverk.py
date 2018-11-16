import string
a = int(input("Hversu mörg: "))

l = []
count = 0
while count < a:
    s = input("Heimilisverk: ")
    if s not in l and s != ' ':
        l.append(s)
    count += 1


print()
for x in l:
    print(x)