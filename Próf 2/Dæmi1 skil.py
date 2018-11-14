

maxLength = 0
longestWord = ""

def open_file(filename):
    file = open(filename, 'r')

def get_longest_word(filename):
    try:
        for word in filename:	# process each line/word
            word = word.strip() # strip leading and trailing white space
            length = len(word)
            if length > maxLength:	 # A new maximum length?
                longestWord = word
                maxLength = length
    except FileNotFoundError:
        print("File", filename, "not found!")

filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream:
	longest_word = get_longest_word(file_stream)
	print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
	file_stream.close
else:
	print('File',filename,'not found!')