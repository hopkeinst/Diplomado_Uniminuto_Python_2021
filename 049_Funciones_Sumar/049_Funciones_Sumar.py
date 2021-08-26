import os
import sys

def limpiar_pantalla():
	sistema_operativo = sys.platform
	if sistema_operativo.startswith('win'):
		os.system("cls")
	else:
		os.system("clear")

def sumar(x, y):
	suma = x+y 
	return suma

limpiar_pantalla()
print("FUNCIONES - CREAR FUNCION SUMAR")
a = None
while a == None:
	try:
		a = float(input("Ingrese el primer número: "))
	except ValueError:
		a = None
		print("-- ERROR -- Ingresaste un valor no numérico.\nInténtelo de nuevo.\n")
b = None
while b == None:
	try:
		b = float(input("Ingrese el segundo número: "))
	except ValueError:
		b = None
		print("-- ERROR -- Ingresaste un valor no numérico.\nInténtelo de nuevo.\n")

print("El resultado de la suma de {:} con {:} es {:}".format(a, b, sumar(a, b)))

print()