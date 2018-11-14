"""Skrifið Python forrit sem les inn lista L af pósitívum heiltölum (e. integers)
og prentar út eftirfarandi upplýsingar:

1. Listann L.
2. Raðaða útgáfu af L.
3. Raðaðan lista af einkvæmum (e. unique) prímtölum í L.
4. Min, max og meðaltal gilda í L.  Meðaltalið skal skrifa út með tveimur aukastöfum.
Þið megið nota listaföll í útfærslunni en þið megið ekki nota neina import setningu.
Fallið is_prime() er gefið.

Prenta þarf út villuskilaboð ef notandinn slær ekki eingöngu heiltölur inn í listann.
Sjá dæmi um inntak/úttak fyrir neðan."""


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



# The main program starts here
L = []
num = (input("Enter integers separated with commas: ")).strip().split(',')
L.append(num)

def list_to_tuple(L): #breyta lista í tuple
        L = []
        L = [int(i) for i in L]
        num = tuple(L)
        L.append(num)
        return(num)

print(list_to_tuple)
total_sum = 0
for value in L:
    total_sum += value
"""if is_prime(num):
    print("{:d} is a prime".format(num))
else:
    print("{:d} is not a prime".format(num))"""

total_sum = sum(L)
average = float(total_sum) / len(L) #tölur í lista teknar og deilt með lengd lista

listi_sorted = L.format()
prime_list = is_prime(L)
print(L)
print(listi_sorted)#sortar listann
print(min(L)) #finnur minnstu tölu í lista
print(max(L)) #finnur stærstu tölu í lista
