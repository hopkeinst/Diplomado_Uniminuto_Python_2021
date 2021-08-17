import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("INTRODUCCIÓN A LAS LISTAS")

miLista = [1, 2.5, "Jorge", [5, 6, -1], 99]

for i in range(len(miLista)):
	print(miLista[i])

print()