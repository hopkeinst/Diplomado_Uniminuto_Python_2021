import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("SUMATORIA DE N^2")

m = 0
while m <=0:
	try:
		m = int(input("Ingrese el número entero positivo 'm' para calcular n^2 desde n=1 hasta n=m: "))
		if m <= 0:
			print("-- ERROR -- Ingresaste un valor menor o igual que cero no válido para la operación.\nInténtalo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no entero.\nInténtalo de nuevo.\n")

resultado = 0
for n in range(1, m+1):
	resultado += (n*n)

print("El fresultado de la sumatoria de n^2 desde n=1 hasta n={:d} es {:d}".format(m, resultado))

print()