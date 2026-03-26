def summa(a,b):
    return a + b

def erotus(a,b):
    return a -b

def tulo (a,b):
    return a * b

def jako (a,b):
    return a / b

print("Tervetuloa käyttämään laskinta <3 ! ")

while True:
    print("Valitse mitä toimintoa haluat käyttää: A: Yhteenlasku B: Vähennyslasku C: Kertolasku D: Jakolasku")

    valinta = input("Valintaasi (A-D, Q lopettaa):")

    if valinta == "Q":
        print("Ohjelma lopetetaan.")
        break
    a = float(input("Anna eka luku:"))
    b = float(input("Anna toinen luku:"))

    if valinta == "A":
        print("Lukujen summa on:", summa(a,b))
    elif valinta == "B":
        print("Lukujen erotus on:", erotus(a,b))
    elif valinta == "C":
        print("Lukujen tulo on:", tulo(a,b))
    elif valinta == "D":
        print("Lukujen osamäärä on:", jako(a,b))
    else:
        print("Virheellinen valinta tai annettu luku.")





