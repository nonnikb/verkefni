n = input("Input a comma separated list: ")
str_arr = n.split(',')
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n%i==0:
            return False
    else:
        return True


def get_prime_list(arr):
    result = []
    for i in arr:
        if is_prime(i):
            result.append(i)
    return list(set(result))

try:
    int_arr = [int(i) for i in str_arr]
    print("Input list: ", end="")
    print(int_arr)
    print('Sorted list: ', end="")
    print(sorted(int_arr))
    print("Prime list: ", end="")
    print(sorted(get_prime_list(int_arr)))
    print("Min: {0}, Max: {1}, Average: {2:.2f}".format(min(int_arr), max(int_arr), sum(int_arr)/len(int_arr)))
except ValueError:
    print("Incorrect input!")
except:
    print("Something strange happened, RUN!")

