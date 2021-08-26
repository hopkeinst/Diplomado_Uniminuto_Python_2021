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
print("FUNCIONES - CALCULO DE COMBINATORIA Y PRODUCTORIA")
n = 0
while n <= 0:
	try:
		n = int(input("Ingrese la población (total elementos): "))
		if n <= 0:
			print("-- ERROR -- No ingresaste un número natural (entero mayor que cero).\nInténtelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un valor no entero.\nInténtelo de nuevo.\n")
r = 0
while r <= 0:
	try:
		r = int(input("Ingrese la cantidad de elementos de la población a los cuales aplicar combinatoria y productoria, este debe ser menor que {:d}: ".format(n)))
		if r <= 0:
			print("-- ERROR -- No ingresaste un número natural (entero mayor que cero).\nInténtelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un valor no entero.\nInténtelo de nuevo.\n")

combinatoria = int(fact(n)/(fact(n-r)*fact(r)))
productoria = int(fact(3)/(fact(n-r)))

print("Combinatoria:",combinatoria)
print("Productoria:",productoria)

print()