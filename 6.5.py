# Kirjoita funktio,
# joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan,
# joka on muuten samanlainen kuin parametrina saatu lista
# paitsi että siitä on karsittu pois kaikki parittomat
# luvut. Kirjoita testausta varten pääohjelma,
# jossa luot listan, kutsut funktiota ja tulostat
# sen jälkeen sekä alkuperäisen että karsitun listan.

lista = [6,87,9,144,20,17]
def parilliset(lista):
    lista2 = []
    for i in lista:
        if (i % 2) == 0:
            lista2.append(i)

    return lista2
parilliset = parilliset(lista)
print(lista)
print(parilliset)