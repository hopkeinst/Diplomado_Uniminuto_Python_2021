import os
import sys
import random as r

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("TABLERO DE AJEDREZ - CABALLO")
print("La idea es generar un tablero de ajedrez 8x8, en el cual en una posición estará un caballo ubicado.\nEl usuario ingresará la posición que quiera que tenga el caballo inicialmente, y a partir de la cual el programa calculará los movimientos posibles y los mostrará en pantalla.\n")

print("Las filas del tablero van de 1 a 8, y las columnas de la letra A a la letra H.\n")
cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
input_ok = True

pos = input("Ingrese la posición que quiera tenga el caballo, fila [1-8], columna[A-H]\nEjemplo => 1,A\nIngreso fila, columna: ").split(",")

if len(pos) != 2:
	print("-- ERROR -- No ingresaste la cantidad de datos solicitados.\nInténtelo de nuevo.\n")
	input_ok = False
else:
	if not(pos[1].upper() in cols):
		input_ok = False
		print("-- ERROR -- No ingresaste un valor de posición correcto.\nInténtelo de nuevo.\n")
	try:
		if not((1 <= int(pos[0]) and (int(pos[0]) <= 8))):
			input_ok = False
	except ValueError:
		print("-- ERROR -- Ingresaste en la parte de la fila un valor no numérico entero.\nInténtelo de nuevo.\n")

while(input_ok == False):
	input_ok = True
	pos = input("Ingrese la posición que quiera tenga el caballo, fila [1-8], columna[A-H]\nEjemplo => 1,A\nIngreso fila, columna: ").split(",")
	input_ok = True
	if len(pos) != 2:
		print("-- ERROR -- No ingresaste la cantidad de datos solicitados.\nInténtelo de nuevo.\n")
		input_ok = False
	else:
		if not(pos[1].upper() in cols):
			input_ok = False
			print("-- ERROR -- No ingresaste un valor de posición correcto.\nInténtelo de nuevo.\n")
		try:
			if not((1 <= int(pos[0]) and (int(pos[0]) <= 8))):
				input_ok = False
		except ValueError:
			print("-- ERROR -- Ingresaste en la parte de la fila un valor no numérico entero.\nInténtelo de nuevo.\n")

tablero = []
for i in range(8):
	fila = []
	for j in range(8):
		fila.append(" ")
	tablero.append(fila)

rC = int(pos[0])-1
cC = cols.index(pos[1].upper())
tablero[rC][cC] = "C"

print("\nTablero con posición inicial del caballo (marcado con 'C'):\n")
print("   ", end="")
for c in cols:
	print("{:^4}".format(c), end="")
print("\n  ", end="")
print("-"*33)
for i in range(8):
	print(" {:1}".format(i+1), end="")
	for j in range(8):
		print("| {:1} ".format(tablero[i][j]), end="")
	print("|")
	print("  ", end="")
	print("-"*33)

mh = 0
mv = 0
for i in range(8):
	if (i%2) == 0:
		mh = 1
		mv = 2
	else:
		mh = 2
		mv = 1
	zona = i//2
	if zona == 0:
		tmh = 1
		tmv = 1
	elif zona == 1:
		tmh = 1
		tmv = -1
	elif zona == 2:
		tmh = -1
		tmv = -1
	else:
		tmh = -1
		tmv = 1
	newR = rC + (mh*tmh)
	newC = cC + (mv*tmv)
	if (newR >= 0) and (newR <= 7) and (newC >= 0) and (newC <= 7):
		#print("Movimiento a:",(newR+1),",",(newC+1))
		tablero[newR][newC] = "X"
print("\nMovimientos posibles del caballo (marcados con 'X'):")
print("   ", end="")
for c in cols:
	print("{:^4}".format(c), end="")
print("\n  ", end="")
print("-"*33)
for i in range(8):
	print(" {:1}".format(i+1), end="")
	for j in range(8):
		print("| {:1} ".format(tablero[i][j]), end="")
	print("|")
	print("  ", end="")
	print("-"*33)

print()