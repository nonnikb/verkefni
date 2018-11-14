import string


# Næ í orð úr file og set þau í lista
def file_to_list(filename):
    try:
        with open(filename, "r") as text_file:  # Opna file-ið sem inputið(filename) segir sem text_file
            word_string = ""  # geri tóman streng
            for line in text_file:
                word_string += line  # tek hverja línu í text_file og bæti því við word_string
            return word_string.split("<NEW DOCUMENT>")  # skipti orðunum í text_file og breyti í listaa
    except FileNotFoundError:
        print("Documents not found")
        quit()


# breyti listanum í dictionary með orðin sem key og númer skjals sem value(s)
def create_dict_from_file(file_content):
    dict_of_words = {}
    for index, document in enumerate(file_content):
        new_word = document.strip().split()
        for word in document.split():
            new_word = word.lower().strip(string.punctuation).strip()
            if new_word in dict_of_words:
                dict_of_words[new_word].add(index)
            else:
                dict_of_words[new_word] = {index}
    return dict_of_words


# leita af orð þar sem input er key
def search_docs(file_dict):
    search_words = input("Enter search words: ").split()
    print("Documents that fit search: ", end="")
    for word in search_words:
        if word in file_dict:
            for key in file_dict[word]:
                doc_number = "".join(str(key))
                doc_number = int(doc_number)-1
                print(doc_number, " ", end="")
    print("\n")


# prenta út númer skjals sem inputið segir til um
def print_documents(file_content):
    doc_number = int(input("Enter document number: "))
    print("Document #{}".format(doc_number))
    document = file_content[doc_number+1]
    print(document)


# hætti í forritinu
def quit_program():
    print("Exiting program.")
    quit()


# velja aðgerð
def choose_action():
    try:
        print("What would you like to do?""\n""1. Search Documents""\n""2. Print Document""\n""3. Quit Program")
        action = int(input("> "))
        return action
    except ValueError:
        return 4



def main():
    # get name of file from user
    #file_name = input("Document collection: ")
    file_name = "dr.txt"
    file_content = file_to_list(file_name)
    file_dict = create_dict_from_file(file_content)
    # choose action
    while True:
        action = choose_action()
        if action == 1:
            search_docs(file_dict)
        elif action == 2:
            print_documents(file_content)
        elif action == 3:
            quit_program()
        else:
            continue


main()