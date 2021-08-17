import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("INTRODUCCIÓN A LAS LISTAS - EXTEND")

lista1 = [1, 3, 5, 7, 9]
lista2 = [0, 2, 4, 6, 8]

print("Lista 1",lista1)
print("Lista 2",lista2)

lista1.extend(lista2)

print("\nLista extendida:",lista1)

print()