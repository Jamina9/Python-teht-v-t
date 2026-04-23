import math

def create_point(x,y):
    return(x,y)

def distance(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    etäisyys = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
    return etäisyys

x1 = float(input("Anna ensimmäisen pisteen x:"))
y1 = float(input("Anna ensimmäisen pisteen y:"))
x2 = float(input("Anna toisen pisteen x :"))
y2 = float(input("Anna toisen pisteen y :"))

piste1 = create_point(x1,y1)
piste2 = create_point(x2,y2)

tulos = distance (piste1, piste2)

print("Pisteiden välinen etäisyys on", tulos)

