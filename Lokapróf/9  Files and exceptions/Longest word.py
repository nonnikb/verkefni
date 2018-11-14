"""Write a program that reads a file named words.txt containing one word per line
with an empty line between sentences. The program prints out the
longest word found in the file along with its length."""




longest = ''

with open("words.txt", "r", encoding = "utf-8") as text_file:
    for word in text_file:
        strip = word.strip().replace(' ', '')
        if len(strip) > len(longest):
            longest = strip


longest_length = len(longest)


print(word)
print("Longest word is", "'"+str(longest)+"'", "of length", str(longest_length))




