# Kirjoita funktio,
# joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen palauttaman summan.

lista = [1,2,5,7,8]

def sivuohjelma(lista):
    for i in lista:
        luku1 = (lista[0])
        luku2 = (lista[1])
        luku3 = (lista[2])
        luku4 = (lista[3])
        luku5 = (lista[4])
        summa = luku1+luku2+luku3+luku4+luku5
        return summa

listansumma = sivuohjelma(lista)
print(listansumma)
