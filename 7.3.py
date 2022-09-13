# Kirjoita ohjelma lentoasematietojen hakemiseksi
# ja tallentamiseksi. Ohjelma kysyy käyttäjältä,
# haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
# ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja
# tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten
# monta kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa
lentokentat = {"EFHK":"Helsinki-vantaa"}

while True:
    userInput = int(input("haluatko syöttää uuden lentoaseman (1), "
                      "hakea jo syötetyn lentoaseman tiedot(2) vai lopettaa(3)."))
    if userInput == 1:
        icao_koodi = input("Anna icao koodi: ")
        lentokentta = input("Anna lentoaseman nimi: ")
        lentokentat[icao_koodi] = lentokentta
        print(lentokentat)
    if userInput == 2:
        Haku = input("Anna haluamasi lentokentän ICAO-koodi: ")
        if Haku in lentokentat:
            print(f"ICAO-koodilla {Haku} lentokentän nimi on {lentokentat[Haku]}")
        else:
            print("Lentokenttä ei ole listassa")
    elif userInput == 3:
        print("Lopetus")
        break


