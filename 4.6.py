# Toteutetaan algoritmi piin (π) likiarvon laskemiseksi.
# Oletetaan, että A on yksikköympyrä eli ympyrä,
# jonka keskipiste on origossa ja jonka säde on yksi.
# Sen ympärille piirretään pienin mahdollinen neliö B siten,
# että ympyrä A jää kokonaan neliön sisäpuolelle.
#  Kirjoita ohjelma,
#  joka kysyy arvottavien pisteiden määrän käyttäjältä ja
#  toteuttaa piin likiarvon laskennan edellä kuvatulla menetelmällä.
#  Lopuksi ohjelma tulostaa piin likiarvon käyttäjälle.

#pisteet = int(input("Anna pisteiden määrä: "))

import turtle
li = list(zip(range(-10,-10),range(10,10)))
xs = [x[0] for x in li]
ys = [x[1] for x in li]
plt.plot(xs,ys)

for i in range(4):
    skk.forward(50)
    skk.right(90)
turtle.done()
