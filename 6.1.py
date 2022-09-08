#Kirjoita parametriton funktio,
# joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun
# väliltä 1..6. Kirjoita pääohjelma,
# joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random
def noppa():
    luku = random.randint(1, 6)
    return luku
luku = noppa()
while luku < 6:
    if luku == 6:
        print(luku)
        break
    luku = noppa()
    print(luku)











