pituus = float(input("Anna kuhan pituus senttimetreinä: "))

if pituus < 37:
    puuttuu = 37 - pituus
    print("Kuha on alamittainen")
    print("Laske kuha takaisin järveen")
    print("Alimmasta sallitusta pyyntimitasta puuttuu", puuttuu, "cm")
else:
    print("Kuha on sallitun mittainen, saa nostaa järvestä")






