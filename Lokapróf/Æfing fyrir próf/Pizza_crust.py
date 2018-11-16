#Flatarmál pi*r**2
#Flatarmál pizzu - innri hringur(crust)
#innri hringur / ytri = prósenta

import math
r, c = input().split()#radíus pizzu
r = int(r)
c = int(c)

f = math.pi*r**2 #heidarflatarmál
rin = r - c # radius innri hrings
fc = math.pi*(rin)**2 #flatarmál innri hrings
pros = (fc/f)*100 #prósenta osts
print(pros)

