def gallona_litroiksi(gallonat):
    return gallonat * 3.785

gallonat = float(input("Anna gallonoiden määrä:"))

while gallonat >= 0:
    litrat = gallona_litroiksi(gallonat)
    print(litrat)

    gallonat = float(input("Anna gallonoiden määrä:"))
