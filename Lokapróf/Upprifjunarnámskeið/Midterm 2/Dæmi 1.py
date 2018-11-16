def get_file_name():
    file_name = input("File Name: ")
    return file_name

longest_word = ""


def get_longest_word(words):
    long_word = ""
    for word in words:
        word = word.strip()
        if len(word) > len(long_word):
            long_word = word
    return long_word

def open_file(file_name):
    file_stream = open(file_name, "r")
    return file_stream

def main():
    filename = get_file_name()
    file_stream = None
    try:
        file_stream = open_file(filename)
        longestword = get_longest_word(file_stream)
        print("{}    {}".format(longestword, len(longestword)))
        file_stream.close()
    except Exception:
        print("File not found!".format(file_name))
main()