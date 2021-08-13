import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("SUMATORIA DE 1/N")

m = 0
while m <=0:
	try:
		m = int(input("Ingrese el número entero positivo 'm' para calcular 1/n desde n=1 hasta n=m: "))
		if m <= 0:
			print("-- ERROR -- Ingresaste un valor menor o igual que cero no válido para la operación.\nInténtalo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no entero.\nInténtalo de nuevo.\n")

resultado = 0.0
for n in range(1, m+1):
	resultado += 1/n

print("El fresultado de la sumatoria de 1/n desde n=1 hasta n={:d} es {:f}".format(m, resultado))

print()