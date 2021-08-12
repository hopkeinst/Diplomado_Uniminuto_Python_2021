import os
import sys
import math as m

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("PRUEBA DEL CICLO WHILE\n")

n = int(input("Ingrese un numero: "))
while(n != 0):
	y = (n*n*n)+1
	print("{:d}^3 + 1 = {:d}".format(n, y))
	n = int(input("\nIngrese un numero: "))

print("FIN")
print()