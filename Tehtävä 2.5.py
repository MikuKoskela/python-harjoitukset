import math
x = float(input("Anna leiviskät"))

y = float(input("Anna naulat"))

z = float(input("Anna luodit"))

leiviskä = x * 20 * 32 * 13.3

naula = y * 32 * 13.3

luoti = z * 13.3

summa = leiviskä + naula + luoti

kilot = math.floor(summa/1000)
grammat = (summa-kilot*1000)

print("Massa nykymittojen mukaan:")
print(kilot, "kilogrammaa ja")
print(grammat, "grammaa")


