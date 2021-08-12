import os
import sys
import math as m

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("PRUEBA DEL CICLO FOR\n")

n = int(input("Ingrese un numero 'n': "))

print("\n\tCiclo FOR con RANGE (1,n+1) = Ciclo repetitivo entre 1 y n: {:d} (inclusive)".format(n))
for i in range(1, n):
	print("i =",i)

print("\n\tCiclo FOR con RANGE (n) = Ciclo repetitivo entre 0 y n: {:d} (sin incluir n)".format(n))
for i in range(n):
	print("i =",i)

print("\n\tCiclo FOR con RANGE (1, n, 2) = Ciclo repetitivo entre 1 y n: {:d} (sin incluir n) incrementando de 2 en 2 el valor de i".format(n))
for i in range(1, n, 2):
	print("i =",i)

print("\n\tCiclo FOR con RANGE (n, -1, -3) = Ciclo repetitivo entre n: {:d} y 0 (decrementando) disminuyendo de 3 en 3 el valor de i".format(n))
for i in range(n, -1, -3):
	print("i =",i)

print()