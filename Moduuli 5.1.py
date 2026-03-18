luvut = []

syöte = input("Anna luku:")
while syöte != "":
    luku = float(syöte)
    luvut.append(luku)

    syöte = input("Anna luku:")

luvut.sort(reverse=True)

for y in range(5):
    print(luvut[y])
