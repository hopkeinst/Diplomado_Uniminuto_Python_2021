import os
import sys
import math as m

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("PROBAR SI DOS NUMEROS SON AMIGOS - TEORÍA 1")

a = 0
while a < 2:
	try:
		a = int(input("Ingrese el numero entero A: "))
		if a < 2:
			print("-- ERROR -- Ingresaste un número menor o igual que 1.\nInténtalo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no numérico.\nInténtalo de nuevo.\n")

b = 0
while b < 2:
	try:
		b = int(input("Ingrese el numero entero B: "))
		if a < 2:
			print("-- ERROR -- Ingresaste un número menor o igual que 1.\nInténtalo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no numérico.\nInténtalo de nuevo.\n")

sumatoria_a = 0
sumatoria_b = 0

for i in range(1, m.ceil((a/2)+1)):
	if (a%i) == 0:
		sumatoria_a += i
for i in range(1, m.ceil((b/2)+1)):
	if (b%i) == 0:
		sumatoria_b += i

print("La suma de los divisores de A: {:d} es {:d}.".format(a, sumatoria_a))
print("La suma de los divisores de B: {:d} es {:d}.".format(b, sumatoria_b))

if (sumatoria_a == b) and (sumatoria_b == a):
	print("Los numeros A: {:d} y B: {:d} SI son amigos.".format(a, b))
else:
	print("Los numeros A: {:d} y B: {:d} NO son amigos.".format(a, b))

print()