import os
import sys
import math as m

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("CALCULO DEL VOLUMEN Y AREA DE LA BASE DE UN CONO")

h = int(input("Ingrese la altura del cono: "))
r = int(input("Ingrese el radio de la base del cono: "))

s1 = m.pi * r * r
s2 = 3.1416 * r * r
v1 = s1 * h / 3
v2 = s2 * h / 3

print("El volumen del cono de altura {:d} y radio {:d} es {:.5f} ({:.5f})".format(h, r, v1, v2))
print("El area de la base del cono es {:.5f} ({:.5f})".format(s1, s2))

print()