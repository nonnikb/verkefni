
def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def even_sum(a_list):
    sum_list = [int(i) for i in a_list if int(i) % 2 == 0]
    return sum(sum_list)

# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
