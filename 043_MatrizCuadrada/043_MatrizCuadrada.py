import os
import sys
import random as r

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("LISTAS DE LISTAS (MATRICES) - MATRIZ CUADRADA")
print("Se creará una matriz cuadrada y se llenará de manera aleatoria con números entre 0 y 9.\n")

n = 0
while n < 1:
	try:
		n = int(input("Ingrese la dimensión de la matriz cuadrada: "))
		if n < 1:
			print("-- ERROR -- No puede existir una matriz con dimensión 0 o negativa.\nInténtelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un valor no entero.\nInténtelo de nuevo.\n")

matrix = []
for i in range(n):
	row = []
	for j in range(n):
		row.append(r.randint(0, 9))
	matrix.append(row)

print("\nMatriz completa:")
for i in range(n):
	print("  ",end="")
	for j in range(n):
		print(matrix[i][j], end="  ")
	print("")

print("\nPrimera fila:\n  ",end="")
for i in range(len(matrix[0])):
	print(matrix[0][i], end="  ")

print("\nÚltima fila:\n  ",end="")
for i in range(len(matrix[-1])):
	print(matrix[-1][i], end="  ")

print("\nPrimera columna:\n  ",end="")
for i in range(len(matrix)):
	print(matrix[i][0], end="  ")

print("\nÚltima columna:\n  ",end="")
for i in range(len(matrix)):
	print(matrix[i][-1], end="  ")

print("\nDiagonal principal:\n  ",end="")
for i in range(len(matrix)):
	print(matrix[i][i], end="  ")

print("\nDiagonal secundaria:\n  ",end="")
for i in range(len(matrix)-1, -1, -1):
	print(matrix[i][len(matrix)-i-1], end="  ")

print()