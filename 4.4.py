# Kirjoita peli,
# jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti,
# kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin
# Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone
# ei saa vaihtaa lukuaan arvauskertojen välissä.
import random

oikea_luku = int(random.randint(1,10))
pelaajan_luku = int(input("Arvaa luku väliltä 1-10: "))

while pelaajan_luku < oikea_luku or oikea_luku < pelaajan_luku:

    if pelaajan_luku < oikea_luku:
        print("Liian pieni arvaus")
        pelaajan_luku = int(input("Arvaa luku väliltä 1-10: "))
    elif pelaajan_luku > oikea_luku:
        print("Liian suuri arvaus")
        pelaajan_luku = int(input("Arvaa luku väliltä 1-10: "))

else:
    print("Oikein")
