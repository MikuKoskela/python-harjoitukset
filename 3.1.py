import math
y = float(input("Kuhan pituus? "))
x = 37
kuha = x-y

if y < x:
    print("Laske kuha takaisin järveen")
    print("Kuha on",kuha,"cm liian pieni")

if x < y:
    print("Onneksi olkoon! " "Kuha on täysi mittainen!")