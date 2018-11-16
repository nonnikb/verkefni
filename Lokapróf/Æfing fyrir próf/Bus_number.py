#s = input()#How many buses
#bnum = input().split()  #bus number

#fyrir stak i á að athuga hvort það mínus eitthvað annað stak =1
#ef satt, athuga hvort að annað stak mínus það stak sé =1
#ef satt, breyta value í tölu1-síðustu tölu
#ef ekki þá bæta value í lista

listi = [1,2,3,5,6]
rod = []
for i in range(len(listi)):
    for j in range(len(listi)):
        if i - j == 1:
            rod.append(i)



print(rod[0],'-',rod[-1])



