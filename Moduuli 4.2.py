syote = input("Anna joku luku:")

pienin = None
suurin = None

while syote != "":
    luku = float(syote)
    if pienin is None:
        pienin = luku
        suurin = luku
    else:
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku

    syote = input("Anna joku luku:")
print("Pienin:", pienin)
print("Suurin:", suurin)
