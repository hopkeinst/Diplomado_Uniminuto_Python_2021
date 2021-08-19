import os
import sys
import random as r

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("ORDENAMIENTO DE LISTAS - MÉTODO BURBUJA (BUBBLE SORT)")
print("Se ordenará una lista de número usando el método de burbuja.\nPara esto se solicitará el tamaño de la lista y posteriormente se llenará aleatoriamente esa lista. Para poderla llenar con números random se solicita el rango de números enteros en que se generarán.\n")

tamano = 0
while tamano <= 0:
	try:
		tamano = int(input("Ingrese tamaño de la lista a ordenar: "))
		if tamano <= 0:
			print("-- ERROR -- Ingresaste un valor menor o igual que cero.\nInténtelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no númerico entero.\nInténtelo de nuevo.\n")
minimo = None
while minimo == None:
	try:
		minimo = int(input("Ingrese el mínimo del rango a generar los números aletarios: "))
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no númerico entero.\nInténtelo de nuevo.\n")
		minimo = None
maximo = None
while maximo == None:
	try:
		maximo = int(input("Ingrese el máximo del rango a generar los números aletarios: "))
		if maximo <= minimo:
			maximo = None
			print("-- ERROR -- Ingresaste un valor haciendo que el máximo tiene un menor valor que el mínimo del rango.\nInténtelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no númerico entero.\nInténtelo de nuevo.\n")
		maximo = None

lista = []
for i in range(tamano):
	lista.append(r.randint(minimo, maximo))
print("Lista inicial => ", end="")
for i in range(len(lista)-1):
	print(lista[i], end=", ")
print(lista[-1])

lista_asc = lista.copy()
lista_desc = lista.copy()

## Bubble sort
for i in range(len(lista_asc)-1, -1, -1):
	for j in range(0, i):
		if lista_asc[j] > lista_asc[j+1]:
			lista_asc[j], lista_asc[j+1] = lista_asc[j+1], lista_asc[j]
print("Lista ordenada de menor a mayor => ", end="")
for i in range(len(lista_asc)-1):
	print(lista_asc[i], end=", ")
print(lista_asc[-1])

## Bubble sort reverse
for i in range(len(lista_desc)-1, -1, -1):
	for j in range(0, i):
		if lista_desc[j] < lista_desc[j+1]:
			lista_desc[j], lista_desc[j+1] = lista_desc[j+1], lista_desc[j]
print("Lista ordenada de mayor a menor => ", end="")
for i in range(len(lista_desc)-1):
	print(lista_desc[i], end=", ")
print(lista_desc[-1])

print()