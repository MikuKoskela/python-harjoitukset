# Kirjoita funktio,
# joka saa parametrinaan bensiinin määrän
# Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan
# vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä
# ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.

def bensiininMäärä(bensiini):
    litroina = (bensiini * 3.78541178)
    return litroina
bensiini = int(input("Anna bensiinin määrä(galloonaa): "))
while bensiini >= 0:
    litrat = bensiininMäärä(bensiini)
    print(litrat)
    bensiini = int(input("Anna bensiinin määrä(galloonaa): "))
if bensiini < 0:
    print("Ohjelma sammuu")