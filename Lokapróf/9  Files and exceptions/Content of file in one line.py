"""Write a program that reads a file calles test.txt and prints out the contents
on the screen after removing all spaces and newlines. Punctuations will
be preserved."""

with open("test.txt", "r") as text_file:
    for line in text_file:
        stripped = line.strip().replace(" ","")
        print(stripped, end="")