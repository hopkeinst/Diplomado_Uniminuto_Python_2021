import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("MATRIZ MÁGICA")
print("Una matriz mágica es aquella que se llena de una manera ordenada especial.\nEste llenado al final hace que la suma de los componentes de sus filas y columnas den el mismo valor.\nPara este caso trabajaremos matrices mágicas de dimensión impar.\n")

dim = 2

while ((dim%2) == 0) or (dim <= 0):
	try:
		dim = int(input("Ingrese la dimensión de la matriz mágica (entero impar): "))
		if (dim%2) == 0:
			print("-- ERROR -- Ingresaste un valor de dimensión que no es impar.\nInténtelo de nuevo.\n")
		elif dim <= 0:
			print("-- ERROR -- Ingresaste un valor de dimensión igual o menor que cero.\nInténtelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un valor no entero.\nInténtelo de nuevo.\n")

matrizMagica = []
for i in range(dim):
	row = []
	for j in range(dim):
		row.append(0)
	matrizMagica.append(row)

iPos = (dim-1)//2
jPos = 0

for p in range(int(dim*dim)): # i -> columna, j -> fila
	matrizMagica[jPos][iPos] = p+1
	jPos -= 1
	iPos += 1
	if iPos >= dim:
		iPos = 0
	if jPos < 0:
		jPos = dim-1

	if matrizMagica[jPos][iPos] != 0:
		iPos -= 1
		jPos += 2
		if iPos < 0:
			iPos = dim-1
		if jPos >= dim:
			jPos = jPos-dim

print("\nMatriz mágica llenada:")
for j in range(dim):
	for i in range(dim):
		print("{:^5}".format(matrizMagica[j][i]), end="")
	print()

print("\nComprobación de las sumas:")
suma_diagonal2 = 0
for i in range(dim-1, -1, -1):
	suma_diagonal2 += matrizMagica[i][len(matrizMagica)-i-1]
print(" "*(5*dim), end="")
print(" ",suma_diagonal2)
print(" "*(5*dim), end="")
print("/")
for j in range(dim):
	suma_filas = 0
	for i in range(dim):
		print("{:^5}".format(matrizMagica[j][i]), end="")
		suma_filas += matrizMagica[j][i]
	print(" =",suma_filas)
for i in range(dim):
	print("{:^5}".format("|"),end="")
print()
for i in range(dim):
	suma_columnas = 0
	for j in range(dim):
		suma_columnas += matrizMagica[j][i]
	print("{:^5}".format(suma_columnas), end="")
print(" \\")
suma_diagonal = 0
for i in range(len(matrizMagica)):
	suma_diagonal += matrizMagica[i][i]
print(" "*(5*dim), end="")
print(" ",suma_diagonal)

print()