import math
hytti_luokka = input("Kirjoita hyttiluokkasi (LUX,A,B,C): ")


if hytti_luokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")

elif hytti_luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")

elif hytti_luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")

elif hytti_luokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka.")
