import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("INTRODUCCIÓN A LAS LISTAS - COUNT")

lista1 = [1, 3, 2, 5, 5, 7, 9, 10, 3, 5, 4, 12, 8]

print("Lista inicial:",lista1)

print("Cantidad de veces que aparece cada elemento")
for i in range(13):
	print(i,"->",lista1.count(i),"veces")

print()