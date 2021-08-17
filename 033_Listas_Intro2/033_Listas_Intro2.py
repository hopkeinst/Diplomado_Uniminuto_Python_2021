import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("INTRODUCCIÓN A LAS LISTAS - AGREGAR ELEMENTOS")

miLista = []

opc = ""

while opc != "no":
	miLista.append(input("Ingrese un dato para ser almacenado en la lista: "))
	opc = (input("\tDesea agregar otro elementos a la lista? (si/no) ")).lower()

print("\nElementos de la lista:")
for i in range(len(miLista)):
	print(i,"->",miLista[i])

print()