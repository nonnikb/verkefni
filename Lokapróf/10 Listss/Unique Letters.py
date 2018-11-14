"""Write a program that makes a list of the unique letters in
an input sentence. That is if the letter "x" is used twice in a
sentence, it should only appear once in your list.
Neither punctuation nor white space should appear in your list."""

import string

s = input("Input a sentence: ")

l = []

for i in s:
    if i not in l and i != ' ':
        l.append(i)

print("Unique letters: ", l)