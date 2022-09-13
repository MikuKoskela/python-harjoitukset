# Kirjoita ohjelma,
# joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
# onko se alkuluku. Alkulukuja ovat luvut,
# jotka ovat jaollisia vain ykkösellä ja itsellään.
kokonaisluku = int(input("Anna kokonaisluku: "))
eiAlkuluku = False
for i in range(2,kokonaisluku):
    luku = kokonaisluku % i
    if luku == 0:
        print("Luku ei ole alkuluku")
        eiAlkuluku = True
        break

if eiAlkuluku:
    print("Luku ei ole alkuluku")
else:
    print("Luku on alkuluku")
