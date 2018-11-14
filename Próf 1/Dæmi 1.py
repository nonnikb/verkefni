"""Skrifið Python forrit sem biður notandann að slá inn nafn skrár sem inniheldur eitt
orð/tóka í línu með auðri línu á milli setninga.  Forritið prentar út lengsta orðið í
skránni ásamt lengd þess.  Ef inntaksskrá finnst ekki þá skal fallið open_file skila
None og aðalforritið prentar þá út viðeigandi villuskilaboð. Aðal forritið er gefið og
því má EKKI breyta."""

# Function definitions start here
longest_word = ''
filename = input("Enter name of file: ") #opnar skrá


open_file = open(filename, 'r')#opnar til að lesa


def get_longest_word(filename):
	#with open(filename, 'r') as f: #opnar til að lesa
	longest_word = ''
	for word in filename:
		stripped = word.strip().replace(' ', '') #skiptir á bili
	if len(stripped) > len(longest_word):
				longest_word = stripped
		#except FileNotFoundError: #ef forritið finnur ekki skrá
		#	print(filename, "not found!")
		#except FileNotFoundError:
		#	print(filename, "not found!")

length_of_longest_word = len(longest_word)

# The main program starts here
filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream:
	longest_word = get_longest_word(file_stream)
	print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
	file_stream.close
else:
	print('File',filename,'not found!')