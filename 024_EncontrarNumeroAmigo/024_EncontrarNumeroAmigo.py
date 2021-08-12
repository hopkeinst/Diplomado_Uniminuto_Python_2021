import os
import sys
import math as m

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("ENCONTRAR UN NUMERO AMIGO A UN NÚMERO A")

a = 0
while a < 2:
	try:
		a = int(input("Ingrese el numero entero A al que desea encontrar su número amigo: "))
		if a < 2:
			print("-- ERROR -- Ingresaste un número menor o igual que 1.\nInténtalo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no numérico.\nInténtalo de nuevo.\n")

# Calcular los divisores y el valor de la sumatoria de estos del número A
sumatoria_a = 0

for i in range(1, m.ceil((a/2)+1)):
	if (a%i) == 0:
		sumatoria_a += i

print("Sumatoria A:",sumatoria_a)

b = m.ceil(m.sqrt(n))
f_amigo = False # Bandera para saber si el número B es o no primo, para detener el ciclo while

while f_amigo == False:
	# Calcular la sumatoria de los divisores de B
	sumatoria_b = 0
	for i in range(1, m.ceil((b/2)+1)):
		if (b%i) == 0:
			sumatoria_b += i
	# Ver si son amigos
	if (sumatoria_a == b) and (sumatoria_b == a):
		f_amigo = True
		print("NÚMERO AMIGO ENCONTRADO !!! El número amigo de {:d} es {:d}".format(a, b))
	else:
		b += 1
	print("B:",b)

print()