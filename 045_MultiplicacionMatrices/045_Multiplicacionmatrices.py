import os
import sys
import random as r
import math as m

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("MULTIPLICACIÓN DE MATRICES")
print("A continuación se realizará la multiplicación de dos matrices.\nPara esto se le solicitará la dimensión de las dos matrices (filas, columnas).\nSi cumplen la condición para la multiplicación de matrices, estas se llenarán de manera aleatoria y se realizará la operación.\n")

row1 = 0
col1 = 0
while row1 <= 0:
	try:
		row1 = int(input("Ingrese la cantidad de filas de la matriz 1: "))
		if row1 <= 0:
			print("-- ERROR -- Ingresaste un valor para filas menor o igual que cero.\nInténtelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no entero.\nInténtelo de nuevo.\n")
while col1 <= 0:
	try:
		col1 = int(input("Ingrese la cantidad de columnas de la matriz 1: "))
		if col1 <= 0:
			print("-- ERROR -- Ingresaste un valor para columnas menor o igual que cero.\nInténtelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no entero.\nInténtelo de nuevo.\n")
row2 = 0
col2 = 0
while row2 <= 0:
	try:
		row2 = int(input("Ingrese la cantidad de filas de la matriz 2: "))
		if row2 <= 0:
			print("-- ERROR -- Ingresaste un valor para filas menor o igual que cero.\nInténtelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no entero.\nInténtelo de nuevo.\n")
while col2 <= 0:
	try:
		col2 = int(input("Ingrese la cantidad de columnas de la matriz 2: "))
		if col2 <= 0:
			print("-- ERROR -- Ingresaste un valor para columnas menor o igual que cero.\nInténtelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no entero.\nInténtelo de nuevo.\n")

if col1 != row2:
	print("-- ERROR -- No se puede calcular la multiplicación de matrices por la condición que la cantidad de columnas de la matriz 1 debe ser igual a la cantidad de filas de la segunda matriz.\nCorra el programa de nuevo y tenga en cuenta esta condición.")
else:
	mat1 = []
	mat2 = []
	for i in range(row1):
		rows = []
		for j in range(col1):
			rows.append(r.randint(0,9))
		mat1.append(rows)
	print("\nPrimera matriz:")
	for i in range(row1):
		for j in range(col1):
			print("{:^3}".format(mat1[i][j]), end="")
		print()
	for i in range(row2):
		rows = []
		for j in range(col2):
			rows.append(r.randint(0,9))
		mat2.append(rows)
	print("\nSegunda matriz:")
	for i in range(row2):
		for j in range(col2):
			print("{:^3}".format(mat2[i][j]), end="")
		print()
	rowR = row1
	colR = col2
	matR = []
	for i in range(rowR):
		rows = []
		for j in range(colR):
			rows.append(m.nan)
		matR.append(rows)
	print("\nCalculo matriz resultante:")
	for i in range(rowR):
		for j in range(colR):
			print("Posicion {:d},{:d} => ".format(i+1,j+1), end="")
			celR = 0
			for k in range(col1):
				if k == (col1-1):
					print("(",mat1[i][col1-1],"*",mat2[col1-1][j],") = ",end="")
				else:
					print("(",mat1[i][k],"*",mat2[k][j],") + ",end="")
				celR += (mat1[i][k]*mat2[k][j])
				matR[i][j] = celR
			print(celR)
	print("\nEntonces, la matriz resultante sería:")
	for i in range(rowR):
		for j in range(colR):
			print("{:^5}".format(matR[i][j]), end="")
		print()

print()