# Kirjoita ohjelma,
# joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa
# silmälukujen summan.
# Käytä for-toistorakennetta.
import random
arpakuutiot = []
kuutio = int(input("Anna arpakuutioiden lukumäärä: "))
nopan_luku = (random.randint(1,6) * kuutio)
arpakuutiot.insert(0, nopan_luku)
for i in arpakuutiot:
    print(f"silmälukujen summa = "
          f"{i}, arpakuutioiden lukumäärä {kuutio}")



