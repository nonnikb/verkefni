def open_file(filename):
    try:
        with open(filename, "r") as text_file:# Opna file-ið sem inputið(filename) segir sem text_file
            word_string = ""# geri tóman streng
            for line in text_file:
                word_string += line# tek hverja línu í text_file og bæti því við word_string
            return word_string.replace("%", "").split()# skipti orðunum í text_file og breyti í lista
    except:
        print("Cannot find file {}".format(filename))
        quit()


def split_to_lists(file):
    parsed_csv = []
    for line in file:
        line_content = []
        state = []
        # read each line and split it into additional list, the outcome should be list with in a list
        for t in line.split(","):
            line_content.append(t)
           # line_content[0].append(state)
        parsed_csv.append(line_content)
    return parsed_csv


def lists_to_values(split_list, place1, place2):
    element_list = []
    for lists in split_list[58::]:
        #print(lists)
        for element in lists[place1:place2]:
            element_list.append(element)
            #print(element_list[0])
    return element_list

#def find_state(min, max):

"""def find_state():
    state = []
    for lists in split_list[58::]:
        if min(lists_to_values(split_list, 1, 2)) in lists:
            state.append(lists)
            print(state)"""



# main()

#filename = input("Enter name of file: ")
filename = "riskFactors.csv"

file = open_file(filename)
split_list = split_to_lists(file)

#place1 = 1
#place2 = place1+1

space = " " * 6
print('{:<33s}{:<33s}{:<6s}'.format('Indicator', 'Min', 'Max'))
print('-' * 87)
print('{:<32s} {:<21s}{:>6}{}{:<15s}{:>6}'.format("Heart Disease Death Rate (2007):", "state", min(lists_to_values(split_list, 1, 2)), space, "state", max(lists_to_values(split_list, 1, 2))))
print('{:<32s} {:<21s}{:>6}{}{:<15s}{:>6}'.format("Motor Vehicle Death Rate (2009):", "state", min(lists_to_values(split_list, 5, 6)), space, "state", max(lists_to_values(split_list, 5, 6))))
print('{:<32s} {:<21s}{:>6}{}{:<15s}{:>6}'.format("Teen Birth Rate (2009):", "state", min(lists_to_values(split_list, 7, 8)), space, "state", max(lists_to_values(split_list, 7, 8))))
print('{:<32s} {:<21s}{:>6}{}{:<15s}{:>6}'.format("Adult Smoking (2010):", "state", min(lists_to_values(split_list, 11, 12)), space, "state", max(lists_to_values(split_list, 11, 12))))
print('{:<32s} {:<21s}{:>6}{}{:<15s}{:>6}'.format("Adult Smoking (2010):", "state", min(lists_to_values(split_list, 13, 14)), space, "state", max(lists_to_values(split_list, 13, 14))))