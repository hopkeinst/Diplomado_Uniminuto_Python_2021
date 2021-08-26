import os
import sys

def limpiar_pantalla():
	sistema_operativo = sys.platform
	if sistema_operativo.startswith('win'):
		os.system("cls")
	else:
		os.system("clear")

def fact(n):
	f = 1
	for i in range(1, n+1):
		f *= i
	return f

limpiar_pantalla()
print("FUNCIONES - FACTORIAL")
n = 0
while n <= 0:
	try:
		n = int(input("Ingrese un número natural al cual calcularle su factorial: "))
		if n <= 0:
			print("-- ERROR -- No ingresaste un número natural (entero mayor que cero).\nInténtelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un valor no entero.\nInténtelo de nuevo.\n")
print("{:d}! = {:d}".format(n, fact(n)))

print()