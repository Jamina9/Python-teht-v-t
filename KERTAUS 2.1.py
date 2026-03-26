luvut = []

uusi_arvo = int(input("Uusi arvo:"))

while uusi_arvo != 0 :
    luvut.append(uusi_arvo)
    print("Lista nyt:", luvut)

    jarjesta = sorted(luvut)
    print("Lista järjestyksessä:", jarjesta)

    uusi_arvo = int(input("Uusi arvo:"))

print("Hei hei!")
