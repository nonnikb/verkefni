
upper = int(input("Enter upper range: "))
prime = []


for num in range(1,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           prime.append(num)

prim3 = upper/3
print(prime)
def prime3(upper):
    

print(prim3)
print(prime3(upper))

total = 0
"""2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61"""