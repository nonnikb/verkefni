s = input().lower().split()
l = []
isgood = True

for i in range(len(s)):
    if s[i] in l:
        isgood = False
    else:
         l.append(s[i])

if isgood:
    print("yes")
else:
    print("no")


n = input("")
word = n.split(" ")
listi = set(word)

if len(listi) < len(word):
    print("no")
else:
    print("yes")