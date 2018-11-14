count = {"UPPER": 0, "LOWER": 0, "NUMBER": 0, "PUNCTUATION": 0, "BIL": 0}
string = input("Enter a sentence: ")

s = len(string)
for i in string:
    if i.isupper():
        count["UPPER"] += 1
    elif i.islower():
        count["LOWER"] += 1
    elif i.isdigit():
        count["NUMBER"] += 1
    elif i.isspace():
        count["BIL"] +=1
    else:
        count["PUNCTUATION"] +=1

print('{:>15}  {:>5}'.format("Upper case", count["UPPER"]))
print('{:>15}  {:>5}'.format("Lower case", count["LOWER"]))
print('{:>15}  {:>5}'.format("Digits", count["NUMBER"]))
print('{:>15}  {:>5}'.format("Punctuation", count["PUNCTUATION"]))
