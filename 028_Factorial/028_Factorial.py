import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("FACTORIAL")

n = 0
while n<=0:
	try:
		n = int(input("Ingrese el número 'n' al cual calcularle su factorial: "))
		if n <= 0:
			print("-- ERROR -- Ingresaste un valor menor o igual que cero no válido para la operación.\nInténtalo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no entero.\nInténtalo de nuevo.\n")

factorial = 1
for i in range(1, n+1):
	factorial *= i

print("El factorial del número {:d} es {:d} ({:d}! = {:d})".format(n, factorial, n, factorial))

print()