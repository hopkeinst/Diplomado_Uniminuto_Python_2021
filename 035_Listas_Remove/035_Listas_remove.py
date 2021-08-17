import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("INTRODUCCIÓN A LAS LISTAS - POP & REMOVE")

lista1 = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8, 1, 3, 5]

print("Lista inicial:",lista1)

lista1.remove(5)

print("Lista despues de remover el primer elemento '5':",lista1)

lista1.pop(5)
lista1.pop(30)

print("Lista despues de remover el elemento de la posicion 5:",lista1)

print()