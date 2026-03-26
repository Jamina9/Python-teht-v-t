def kertotaulu(luku):
    for i in range(1,11):
        print(luku,"*",i, "=", luku * i)

numero = int(input("Anna jokin luku väliltä 1-10:"))
kertotaulu(numero)

