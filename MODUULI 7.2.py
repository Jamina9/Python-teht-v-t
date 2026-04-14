lentoasemat = {}

while True:
    toiminto = input("Valitse jokin toiminto( 1 = Syötä uuden lentoaseman tiedot, 2 = Hae lentoaseman tiedot, 3 = Lopeta käyttäminen):")

    if toiminto == "1":
        ICAO = input ("Anna ICAO-koodi:")
        nimi = input("Anna lentoaseman nimi:")
        lentoasemat[ICAO] = nimi

    elif toiminto == "2":
        ICAO = input("Anna ICAO-koodi:")
        print(lentoasemat[ICAO])

    elif toiminto == "3":
        break

