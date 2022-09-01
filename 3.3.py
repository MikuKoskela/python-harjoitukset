
gender = input("Sukupuolesi (nainen/mies)? ")
hg_value = int(input("Hemoglobiini (g/l)? "))

if gender == "nainen":
    if hg_value < 117:
        print(f"Hemoglobiiniarvo:" ,hg_value, "(g/l) on alhainen.")
    elif hg_value <= 175:
        print(f"Hemoglobiiniarvo:" ,hg_value, "(g/l) on normaali. ")
    else:
        print(f"Hemoglobiiniarvo" ,hg_value, "(g/l) on korkea.")

elif gender == "mies":
    if hg_value < 134:
        print(f"Hemoglobiiniarvo:" ,hg_value, "(g/l) on alhainen.")
    elif hg_value <= 195:
        print(f"Hemoglobiiniarvo:" ,hg_value, "(g/l) on normaali. ")
    else:
        print(f"Hemoglobiiniarvo" ,hg_value, "(g/l) on korkea.")

else:
    print("Vastaus virheellinen")


