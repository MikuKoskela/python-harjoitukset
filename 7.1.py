# Kirjoita ohjelma,
# joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
# (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat
# merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi
# siten, että joulukuu on ensimmäinen talvikuukausi.

kuukaudet = ("Joulukuu","Tammikuu","Helmikuu","Maaliskuu",
             "Huhtikuu","Toukokuu","Kesäkuu","Heinäkuu",
             "Elokuu","Syyskuu","Lokakuu","Marraskuu",)
kuukausi_numero = int(input("Anna kuukauden numero(1-12): "))
kuukausi = (kuukaudet[kuukausi_numero-1])
if kuukausi_numero <= 3:
    print(f"Kuukauden {kuukausi} vuodenaika on Talvi.")
elif kuukausi_numero <= 6:
    print(f"Kuukauden {kuukausi} vuodenaika on Kevät.")
elif kuukausi_numero <= 9:
    print(f"Kuukauden {kuukausi} vuodenaika on Kesä.")
elif kuukausi_numero >= 9:
    print(f"Kuukauden {kuukausi} vuodenaika on Syksy.")
