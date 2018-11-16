def make_sublist(a_list):
    result = [[]]
    for i in range(len(a_list)):
        for j in range(i, len(a_list)):
            sublist = a_list[i:j + 1]
            result.append(sublist)
    return result

def read_list():
    lst = input("Input a comma separated list: ")
    return lst.split(",")

my_list = read_list()
sub_lists = make_sublist(my_list)

print(sub_lists)