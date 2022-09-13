# Kirjoita ohjelma,
# joka kysyy käyttäjältä nimiä.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa,
# joko tekstin Uusi nimi tai Aiemmin syötetty nimi
# sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan
# allekkain mielivaltaisessa järjestyksessä.
# Käytä joukkotietorakennetta nimien tallentamiseen.
nimet = set()
userInput = input("Anna nimi: ")
while userInput != "":
    if userInput in nimet:
        print(f"Aiemmin syötetty nimi: {userInput}")
    if userInput not in nimet:
        print(f"Uusi nimi: {userInput}")
    nimet.add(userInput)
    userInput = input("Anna nimi: ")
for n in nimet:
    print(n)


