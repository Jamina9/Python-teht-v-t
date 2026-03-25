import random

def heita_noppaa():
    return random.randint(1,6)
silmäluku = 0

while silmäluku != 6:
    silmäluku = heita_noppaa()
    print(silmäluku)
