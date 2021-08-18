import os
import sys
import random as r

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("INTRODUCCIÓN A LAS LISTAS - EJERCICIO 1")
print("Generar una lista de 100 números aleatorios entre 10 y 500.\nCalcular la media y la moda del conjunto de números generados.")

numeros = []

for i in range(100):
	numeros.append(r.randint(10, 50))

promedio = 0
cnt_moda = 0
numeros.sort()
moda = []
for n in numeros:
	promedio += n
	if numeros.count(n) > cnt_moda:
		moda = []
		cnt_moda = numeros.count(n)
		moda.append(n)
	elif numeros.count(n) == cnt_moda:
		if not(n in moda):
			moda.append(n)

promedio = promedio / 100

print("Promedio de numeros:",promedio)
print("Moda de la lista:",moda,"apareciendo",cnt_moda,"veces")

print("\n---------------------------------------------------")
print("COMPROBACION DE DATOS")
cnt_cols = 1
for i in range(10,51):
	print(i,"->",numeros.count(i),"veces", end="\t")
	cnt_cols += 1
	if cnt_cols > 6:
		print()
		cnt_cols = 1


print()