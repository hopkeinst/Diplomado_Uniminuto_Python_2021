import os
import sys
import random as r

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("LISTAS - ELIMINAR IMPARES")
print("Se va a crear una lista con 20 elementos aleatorios entre 0 y 9, y eliminar los impares.\n")

lista = []
for i in range(20):
	lista.append(r.randint(0, 9))

print("Lista inicial => ", end="")
for i in range(len(lista)-1):
	print(lista[i], end=", ")
print(lista[-1])

impares = []
for i in range(len(lista)):
	if lista[i]%2 == 1:
		impares.append(lista[i])
for i in impares:
	lista.remove(i)
print("Lista modificada => ",end = "")
for i in range(len(lista)-1):
	print(lista[i], end=", ")
print(lista[-1])

print()