henkilöt = { "John": ["John", 30, "Engineer"],
             "Emily":["Emily",25, "Artist"],
             "Anna": ["Anna", 22, "Student"]}

print("Johnin nimi ja ikä on:", henkilöt["John"][0], henkilöt["John"][1])
print("Emilyn ammatti on:", henkilöt["Emily"][2])

henkilöt["Anna"][2] = "Teacher"
henkilöt["James"] = ["James", 28, "Writer"]
henkilöt["Sophia"] = ["Sophia" , 35 , "Doctor"]

del henkilöt["Emily"]


for nimi in henkilöt:
    print(nimi, henkilöt[nimi])


