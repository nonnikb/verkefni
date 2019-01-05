l = []
name = []
with open("flights.txt") as f:
    for line in f:
        l.append(line)
        name.append(line.split()[0])


print(l)
print(set(name))
ans = ""

ans += l[0]

for i in range(1, len(l)):
    if l[i] != l[i-1]:
        ans += l[i]

print(ans)
"""
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        ans += s[i]
def open_file(filename):
    fl = open(filename.txt)
    return fl

def find_key(a_dict, key):
    try:
        print("Value: ", a_dict[key])

for i in range(len(name)):
    print(set(name))
    for city in"""