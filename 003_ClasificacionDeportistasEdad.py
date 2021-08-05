import os
import sys
import math as m

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("CLASIFICACION DE DEPORTISTAS POR EDAD")

edad = int(input("Ingrese la edad del deportista, en años: "))

if edad <= 14:
	print("La categoría del deportista es PREJUVENIL")
elif edad <= 18:
	print("La categoría del deportista es JUVENIL")
else:
	print("La categoría del deportista es MAYORES")

print()