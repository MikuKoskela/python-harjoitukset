# Kirjoita ohjelma,
# joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
# onko se alkuluku. Alkulukuja ovat luvut,
# jotka ovat jaollisia vain ykkösellä ja itsellään.
kokonaisluku = int(input("anna kokonaisluku: "))

for i in range(2,kokonaisluku//2+1):

    if (kokonaisluku % i) == 0:
        print("Luku ei ole alkuluku")
        break
    elif (kokonaisluku % i) == 1:
        print("luku on alkuluku")
        break
