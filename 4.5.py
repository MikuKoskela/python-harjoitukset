# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin,
# tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein
# tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja
# jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).

userinput = input("Syötä käyttäjätunnus:")
passwordinput = input("Syötä salasana:")
yritykset = 1

if userinput != "python" or passwordinput != "rules":
    while yritykset < 5:
        print("Yritä uudelleen")
        yritykset = yritykset + 1
        userinput = input("Syötä käyttäjätunnus:")
        passwordinput = input("Syötä salasana:")

if userinput == "python" and passwordinput == "rules":
    print("Tervetuloa")

else:
    print("Pääsy evätty")

