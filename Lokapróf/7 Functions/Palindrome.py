"""A palindrome is a word, phrase, number or other sequence
of characters which reads the same backward as forward
such as: madam or racecar.
Sentence-length palindromes may be written when allowances
are made for adjustments to capital letters, punctuation
and word dividers, such as "A man, a plan, a canal, Panama!"
Write a function that takes a string as an argument and returns
True if the string is a palindrome and False otherwise.
Also write code that calls the function with the input as an
argument and prints out the appropriate message. """

def is_pal(s):
    s = s.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace('"', "").replace ("'", "").lower()
    if s == s[::-1]:
        return True
    else:
        return False


s = input("Enter a string: ")
if is_pal(s):
    print('"'+s+'"', "is a palindrome.")
else:
    print('"'+s+'"', "is not a palindrome.")