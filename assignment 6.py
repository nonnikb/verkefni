def find_vowel(word):
    for i in range(len(word)):
       if word[i] in VOWELS:
         return i
    return -1

my_str = word


VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
ordid = " "
while ordid != ".":
    ordid = input("Enter a word: ")

    words = ordid.split()
    count = 0

    for word in words:
        vowel = find_vowel(word)
        if( ordid == "." ):
            break
        elif(vowel == -1):
            print(word + "ay")
        elif(vowel == 0):
            print(word + "yay")
        else:
            print(word[vowel:] + word[:vowel] + "ay")