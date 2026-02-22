Sukupuoli = input("Kerro biologinen sukupuolesi:")
Hemoglobiini = float(input("Kerro hemoglobiiniarvosi:"))

if Sukupuoli == "nainen":
    if Hemoglobiini < 117:
        print("Hemoglobiini on alhainen")
    elif Hemoglobiini > 175:
        print("Hemoglobiini on normaali")
    else:
        print("Hemoglobiini on korkea")

if Sukupuoli == "mies":
    if Hemoglobiini < 135:
        print("Hemoglobiini on alhainen")
    elif Hemoglobiini > 196:
        print("Hemoglobiini on normaali")
    else:
        print("Hemoglobiini on korkea")
