def suurin_luku(luku1, luku2, luku3):
    suurin = luku1

    if luku2 > suurin:
        suurin = luku2

    if luku3 > suurin:
        suurin = luku3

    return suurin

luku1 = int(input("Anna ensimmäinen luku:"))
luku2 = int(input("Anna toinen luku:"))
luku3 = int(input("Anna kolmas luku:"))

tulos = suurin_luku(luku1, luku2, luku3)
print("Suurin luku on", tulos)


