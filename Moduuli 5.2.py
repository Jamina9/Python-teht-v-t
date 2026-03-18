luku = int(input("Anna jokin luku:"))

on_alkuluku = True
for y in range(2,luku):
    if luku % y == 0:
        on_alkuluku = False

if on_alkuluku:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")
