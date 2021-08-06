import os
import sys
import math as m

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("CONTADOR Y ACUMULADOR DE LA EDAD DE LAS PERSONAS")

edad_total = 0
cnt_personas = 0

maxima_edad = int(input("Ingrese la edad maxima a la que quiere que pare: "))

edad = int(input("\tIngrese la edad:"))
while (edad_total + edad) <= maxima_edad:
	print("\t --> Siga")
	edad_total += edad
	cnt_personas += 1
	edad = int(input("\tIngrese la edad: "))

print("Ya no pueden ingresar mas personas")

print("\nEdad total maxima: {:d}".format(edad_total))
print("Cantidad de personas que ingresaron: {:d}".format(cnt_personas))

print()