import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("INTRODUCCIÓN A LAS LISTAS - ELIMINAR REPETIDOS EN LA LISTA")

lista1 = [1, 3, 2, 5, 5, 7, 9, 10, 3, 5, 4, 12, 8]

print("Lista inicial:",lista1)

for i in lista1:
	rep = lista1.count(i)
	for j in range(1,rep):
		lista1.remove(i)

print("Lista depurada de repetidos:",lista1)

print("\n\nPara una lista de 1.000 elementos aleatorios")

import random

lista2 = []
for i in range(1000):
	lista2.append(random.randint(1, 1000))

print("Largo de la lista inicial:",len(lista2))
cnt_repetidos = 0
for i in lista2:
	rep = lista2.count(i)
	for j in range(1,rep):
		lista2.remove(i)
		cnt_repetidos += 1
print("Largo de la lista despues de depurada:",len(lista2))
print("Se eliminaron",cnt_repetidos,"elementos repetidos de la lista")

print()