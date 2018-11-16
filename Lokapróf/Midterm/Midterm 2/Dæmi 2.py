def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

def get_data():
    try:
        a_list = [int(x) for x in input("Enter nums").split(',')]
        return a_list
    except ValueError:
        print("False")

my_list = get_data()
sort = my_list[:]
list_sorted = sorted(sort)

def prime_list(listi):
    prime_listi = []
    for num in listi:
        if is_prime(num) and num not in prime_listi:
            prime_listi.append(num)
    return prime_listi

print("Input list: ", my_list)
print("Sorted list: ", list_sorted)
print("Prime list: ", prime_list(my_list))
print("Min:", min(my_list), "Max: ", max(my_list), "Average: ", ("%.2f" % (sum(my_list)/len(my_list))))

print("min: {} max: {} average: {:.2f}".format(min(my_list), max(my_list), sum(my_list)/len(my_list)))

