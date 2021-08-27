import os
import sys

def limpiar_pantalla():
	sistema_operativo = sys.platform
	if sistema_operativo.startswith('win'):
		os.system("cls")
	else:
		os.system("clear")

def fib(c, n, a, b):
	if n > 1:
		f = a + b
		c += 1
		n -= 1
		print(c,"->",f)
		a = b 
		b = f
		fib(c, n, a, b)
	else:
		return None

limpiar_pantalla()
print("N ELEMENTOS FIBONACCI")

n = 0
while n <= 0:
	try:
		n = int(input("Ingrese la cantidad de elementos de la serie Fibonacci que desea conocer: "))
		if n <= 0:
			print("-- ERROR -- Ingresaste un número menor o igual que cero.\nInténtelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no numérico entero.\nInténtelo de nuevo.\n")

print("1 -> 1")
if n > 1:
	fib(1, n, 0, 1)

print()