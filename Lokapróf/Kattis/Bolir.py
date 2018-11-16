import string
a = int(input("Hversu mörg: "))

l = []
f = []
count = 0
while count < a:
    n = input("Nafn: ")
    s = input("Staðsetning: ")
    #if s not in l and s != ' ':
    l.append(s)
    count += 1


print()
for x in l:
    print(x)
    print(set(len(f)))