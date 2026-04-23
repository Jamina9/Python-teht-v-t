oppilaat = {"Matti": ["Matti", 9, "Matematiikka"],
            "Liisa": ["Liisa", 8 , "Englanti"]}

print("Matin vuosiluokka on:", oppilaat["Matti"][1])
print("Liisan lempiaine on:", oppilaat["Liisa"][2])

oppilaat["Matti"][2] = "Fysiikka"
oppilaat["Pekka"] = ["Pekka", 7, "Historia"]

del oppilaat["Liisa"]

for nimi in oppilaat:
    print(nimi, oppilaat[nimi])
