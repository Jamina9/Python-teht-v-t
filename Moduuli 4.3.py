import random

vastaus = random.randint(1,10)
arvaus = int(input("Arvaa luku 1-10:"))

while arvaus != vastaus:
    if arvaus < vastaus:
        print("Liian pieni arvaus")

    if arvaus > vastaus:
        print("Liian suuri arvaus")

    arvaus = int(input("Arvaa luku 1-10:"))

print("Oikein!")

