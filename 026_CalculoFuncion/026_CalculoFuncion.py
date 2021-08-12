import os
import sys
import math as m

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("CALCULAR VALORES DE UNA FUNCION")

funcion = input("Ingrese la función a evaluar.\n  Escríbala en término de 'x' y especificando cada operación => ")

x1 = None
while x1 == None:
	try:
		x1 = int(input("Ingrese el rango menor de 'x' a evaluar, entero: "))
	except:
		print("-- ERROR -- Ingresaste un valor no numérico.\nInténtelo de nuevo.\n")
		x1 = None

x2 = None
while x2 == None:
	try:
		x2 = int(input("Ingrese el rango mayor de 'x' a evaluar, entero: "))
	except:
		print("-- ERROR -- Ingresaste un valor no numérico.\nInténtelo de nuevo.\n")
		x2 = None

if x1 < x2:
	step = 1
else:
	step = -1
print("-"*14)
print("|{:^5s}|{:^6s}|".format("x","f(x)"))
print("-"*14)
for x in range(x1, x2+1, step):
	resultado = eval(funcion)
	resultado2 = (x*x) - (2*x) + 1
	print("|{:^5d}|{:^6d}|".format(x, resultado))	
print("-"*14)

print()