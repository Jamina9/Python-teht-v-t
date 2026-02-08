import math
print(math.pi * 3)

sade_str = input("Kerro ympyrän sade: ")
sade = float(sade_str)
pinta_ala = math.pi * sade ** 2
print(pinta_ala)

Kanta = input("Anna kanta:")
Kanta = float(Kanta)
Korkeus = input("Anna Korkeus:")
Korkeus = float(Korkeus)
Piiri = 2*Kanta*Korkeus
Pinta_ala = Kanta*Korkeus
print("pinta_ala",Pinta_ala)
print("piiri",Piiri)



