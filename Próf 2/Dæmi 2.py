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

"""def list_to_tuple(L): #breyta lista í tuple
    try:
        L = [int(i) for i in L]
        a_tuple = tuple(L)
        return(a_tuple)
    except ValueError:
        print("Error. Please enter only integers.")
        return ()"""


# The main program starts here

num = input("Enter integers separated with commas: ").strip().split(',')
L = []
L.append(num)
print(L)

for i in range(num):
    value = int(input("value no.{} ".format(i + 1)))
    L.append(value)

highest_value = max(L) #finna stærsta gildi
lowest_value = min(L) #finna lægsta gildi
total_sum = sum(L) #summa gilda
average = float(total_sum) / len(L) #meðaltal

"""print("Input list: ", L)
print("Sorted list: ", L.sort())
print("Prime list: ", L)
print("Min: ", lowest_value, "Max: ", highest_value, "Average: ", average)"""

"""2,5,7,2,8,10,34,23,9,4,5"""