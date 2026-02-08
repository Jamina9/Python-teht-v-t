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

Luku1 = int(input("Anna Luku1:"))
Luku2 = int(input("Anna Luku2:"))
Luku3 = int(input("Anna Luku3:"))
summa = Luku1 + Luku2 + Luku3
tulo = Luku1 * Luku2 * Luku3
keskiarvo = summa / 3
print(summa)
print(tulo)
print(keskiarvo)

Leiviska = int(input("Anna Leiviska:"))
Naula = int(input("Anna Naula:"))
Luoti = int(input("Anna Luoti:"))
Luodit_yht = Leiviska * 20*32 + Naula * 32 + Luoti
Grammat_yht = Luodit_yht * 13.3
Kilogrammat = int(Grammat_yht // 1000)
Grammat = Grammat_yht - Kilogrammat * 1000
print(Grammat)
print(Kilogrammat)






