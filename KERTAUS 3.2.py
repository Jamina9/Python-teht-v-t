kirjasto = {"Suon villi laulu": ["Delia Owens", 2018, "Romaani"],
            "Lehmä synnyttää yöllä": ["Pajtim Statovci", 2019, "Romaani"],
            "Missä metsä kohtaa tähdet": ["Glendy Vanderah", 2019, "Romaani"]}

print("Suon villi laulu kirjailija on:", kirjasto["Suon villi laulu"][0])
print("Missä metsä kogtaa tähdet kirjan genre on:", kirjasto["Missä metsä kohtaa tähdet"][2])

kirjasto["Suon villi laulu"][2] = "Esikoisromaani"

kirjasto["Majakka"] = ["Christian Rönnbacka", 2020, "Rikos"]

del kirjasto["Lehmä synnyttää yöllä"]

for kirja in kirjasto:
    print(kirja, kirjasto[kirja])
