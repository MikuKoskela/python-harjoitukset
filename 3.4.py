#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
#Vuosi on karkausvuosi, jos se on jaollinen neljällä.
#Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi_luku = int(input("Anna vuosiluku: "))
karkaus_vuosi = vuosi_luku % 4
sadalla_jaolliset = vuosi_luku % 400

if sadalla_jaolliset == 0:
    print(f"Vuosiluku", vuosi_luku, "on karkausvuosi.")

elif karkaus_vuosi == 0:
    print(f"Vuosiluku",vuosi_luku, "on karkausvuosi." )
else:
    print(f"Vuosiluku",vuosi_luku, "ei ole karkausvuosi." )