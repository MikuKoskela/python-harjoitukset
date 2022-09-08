# Kirjoita funktio,
# joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa
# pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat
# ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle
# (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen
# laskennassa on hyödynnettävä kirjoitettua funktiota
import math
pizza1 = int(input("Anna pizzan 1. halkaisija: "))
pizza1_hinta = int(input("Anna pizzan 1. hinta: "))
pizza2 = int(input("Anna pizzan 2. halkaisija: "))
pizza2_hinta = int(input("Anna pizzan 1. hinta: "))
def laskuri(pizza1,pizza1_hinta,pizza2,pizza2_hinta):
    pizza1 = pizza1 * math.pi
    pizza1_hinta = pizza1 * pizza1_hinta / pizza1
    pizza2 = pizza2 * math.pi
    pizza2_hinta = pizza2 * pizza2_hinta / pizza2
    if pizza1_hinta < pizza2_hinta:
        return print(f"Pizzalla 1. on halvempi hinta: {pizza1_hinta}(e/m^2)")

    elif pizza2_hinta < pizza1_hinta:
        return print(f"Pizzalla 2. on halvempi hinta: {pizza2_hinta}(e/m^2)")
laskuri(pizza1,pizza1_hinta,pizza2,pizza2_hinta)


#if pizza1_hinta < pizza2_hinta:
 #   print(f"Pizzalla 1. on halvempi hinta: {hinta}(e/m^2)")
#elif pizza2_hinta < pizza1_hinta:
 #   print(f"Pizzalla 2. on halvempi hinta: {hinta}(e/m^2)")
