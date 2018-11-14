vowels = ('a','e','i','o','u', 'y', 'A', 'E', 'I', 'O', 'u', 'y')
x = 1

while x == 1:
    word = input('Enter a word:')
    i = 0

    for w in word:
        if w in vowels:
            break
        i = i+1

    if i==0:
        print(word[:] + 'ay')
    else:
        print(word[i:] + word[:i] + 'ay')