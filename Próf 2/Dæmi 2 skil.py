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


def get_list():
    L = input("Enter elements of list separated by commas: ").strip().split(',')
    L = [int(i) for i in L]
    return L

# Main program starts here - DO NOT change it
L = get_list()
print(L)

highest_value = max(L) #finna stærsta gildi
lowest_value = min(L) #finna lægsta gildi
total_sum = sum(L) #summa gilda
average = float(total_sum) / len(L) #meðaltal
sorted = L.sort()


print("Input list: ", L)
print("Sorted list: ", sorted)
print("Prime list: " is_prime(L))
print("Min:", lowest_value, "Max:", highest_value, "Average:", average)