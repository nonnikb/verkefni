"""Skrifið Python forrit sem les inn tvær heiltölur frá notanda. Fyrri talan stendur fyrir upphafsgildi
á röð og seinni talan stendur fyrir mismun á sérhverjum samliggjandi gildum raðarinnar.
Forritið skrifar síðan út sérhvert gildi raðarinnar (með einu bili á milli gilda) þangað til summa gildanna
er orðin >= 100. Í lokin skrifast jafnframt út summan.

Inntak/úttak forritsins á að vera nákvæmlega eins og fram kemur í dæminu hér fyrir neðan."""

initial = int(input("Initial value: "))
step = int(input("Step: "))

x = initial
num = 0
sum = 0

print(initial, end=" ")
while sum <= 100:
    print(x + step, end=" ")
    x = (x + step)
    sum = sum + x
print("")

print("Sum of series: ", sum + initial)