import string

sentence = input("Input a sentence: ")
text = sentence.split(".")
unique_letters=[]
for sentence in text:
    for unique_letter in sentence:
        if unique_letter not in unique_letters and unique_letter.isalpha():
            unique_letters.append(unique_letter)
# Here you should add the missing part
print("Unique letters:", unique_letters)