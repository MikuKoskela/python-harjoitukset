# Kirjoita ohjelma, joka kysyy käyttäjältä
# viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen)
# ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet
# yksi kerrallaan allekkain samassa järjestyksessä kuin
# ne syötettiin. käytä for-toistorakennetta nimien kysymiseen
# ja for/in toistorakennetta niiden läpikäymiseen.

kaupungit = []
kerrat = 5
for i in range(0,kerrat):

    if len(kaupungit) < 5:
        kaupunki = input("Anna kaupungin nimi: ")
        kaupungit.insert(5,kaupunki)
for kaupunki in kaupungit:
    print(kaupunki)