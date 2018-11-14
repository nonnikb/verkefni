

with open("test.txt", "r") as text_file:
    for line in text_file:
        stripped = line.strip().replace(" ", "")
        print(stripped, end="")

