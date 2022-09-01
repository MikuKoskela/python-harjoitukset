# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi
# niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa.

tuuma = float(input("Anna tuumat "))
sentti_metri = tuuma * 2.54
while tuuma > 0:
    print(f"",tuuma,"tuumaa on ",sentti_metri,"cm.")
    tuuma = float(input("Anna tuumat "))
    sentti_metri = tuuma * 2.54
else:
    print("Ohjelma lopettaa toimintansa.")