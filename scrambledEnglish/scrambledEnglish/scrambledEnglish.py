import random
import string

# Næ í orð úr file og set þau í lista
def get_word_string(filename):
    try:
        with open(filename, "r") as text_file:# Opna file-ið sem inputið(filename) segir sem text_file
            word_string = ""# geri tóman streng
            for line in text_file:
                word_string += line# tek hverja línu í text_file og bæti því við word_string
            return word_string.split()# skipti orðunum í text_file og breyti í lista
    except:
        print("File {} not found".format(filename))# printar út filename ef það er ekki neitt file
        return ""

#tek orð úr lista og segi til um hvort þau innihalda "punctuation"
def word_in_punctuation(get_word_string):
    for word in word_string:
        if len(word) >= 4:
            if word[-1] in string.punctuation:
                return -1
            else:
                return -2

# tek orð úr lista, scrambla þau og breyti svo í streng
def scramble_string(get_word_string):
    listi = []  # tómur listi
    for word in word_string:
        if len(word) >= 4:
            first = word[0]
            last = word[word_in_punctuation(get_word_string):] #tek ytri stafina frá
            word_middle = list(word[1:word_in_punctuation(get_word_string)]) # tek miðjuna úr orðunum
            random.shuffle(word_middle)  # shuffla orðin
            word_middle = first + "".join(word_middle) + last# breyti orðunum úr lista í streng og bæti ytri stöfnum við
            listi.append(word_middle)# bæti orðin við listi (tóma listann)
        else:
            listi.append(word)# bæti orðin við listi (tóma listann)
    return " ".join(listi)  #breyti listanum í string

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)