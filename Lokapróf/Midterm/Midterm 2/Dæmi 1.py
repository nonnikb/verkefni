
def get_file_name():
        filename = input("File name: ")
        return filename


def open_file(filename):
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return False


def get_longest_word(words):
    longest = ""
    for word in words:
        word = word.strip()
        if len(word) > len(longest):
            longest = word
    return longest

"""#with open("words.txt", "r", encoding = "utf-8") as text_file:
    for word in text_file:
        strip = word.strip().replace(' ', '')
        if len(strip) > len(longest):
            longest = strip"""


# The main program starts here
filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream:
	longest_word = get_longest_word(file_stream)
	print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
	file_stream.close
else:
	print('File',filename,'not found!')