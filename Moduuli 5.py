import random

Lukumäärä = int(input("Anna arpakuutioiden lukumäärä:"))
summa = 0

for y in range(Lukumäärä):
    silmäluku = (random.randint(1,6))
    summa = summa + silmäluku

print("Silmälukujen summa on", summa)



