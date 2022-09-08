import random

tahkot = int(input("Anna nopan tahkot: "))
def noppa(tahkot):
    luku = random.randint(1, tahkot)
    return luku

luku = noppa(tahkot)
while luku < tahkot:
    if luku == tahkot:
        print(luku)
        break
    luku = noppa(tahkot)
    print(luku)