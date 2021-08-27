import os
import sys

def limpiar_pantalla():
	sistema_operativo = sys.platform
	if sistema_operativo.startswith('win'):
		os.system("cls")
	else:
		os.system("clear")

def fib(c, n, a, b):
	f = a + b
	if f <= n:
		c += 1
		n -= 1
		print(c,"->",f)
		a = b 
		b = f
		fib(c, n, a, b)
	else:
		return None

limpiar_pantalla()
print("ELEMENTOS FIBONACCI MENORES O IGUALES QUE N")

n = 0
while n <= 1:
	try:
		n = int(input("Ingrese el valor del cual desee conocer los números de la serie Fibonacci menores o iguales a este: "))
		if n <= 1:
			print("-- ERROR -- Ingresaste un número menor o igual que uno.\nInténtelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no numérico entero.\nInténtelo de nuevo.\n")

print("1 -> 1")
print("2 -> 1")
if n > 2:
	fib(2, n, 1, 1)

print()