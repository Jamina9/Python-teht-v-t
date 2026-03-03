yrityksiä = 0

tunnus = input("Anna käyttäjätunnus:")
salasana = input("Anna salasana:")

while (tunnus != "python" or salasana != "rules") and yrityksiä < 4:
    yrityksiä = yrityksiä + 1

    tunnus = input("Anna käyttäjätunnus:")
    salasana = input("Anna salasana:")

if tunnus == "python" and salasana == "rules":
    print("Tervetuloa !")
else:
    print("Pääsy evätty.")
