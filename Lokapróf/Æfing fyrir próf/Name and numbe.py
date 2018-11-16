
def enter_data(the_dict):
    name = input("Name: ")
    number = input("Number: ")
    the_dict[name] = number


def more_data():
    more = input("More data (y/n): ")
    return more.lower() == 'y'

def dict_to_tuple(the_dict):
    dictlist = []
    for key, value in the_dict.items():
        temp = (key, value)
        dictlist.append(temp)
    return dictlist

the_dict = {}

play = True
while play:
    enter_data(the_dict)
    play = more_data()

dictlist = dict_to_tuple(the_dict)
print(dictlist)



