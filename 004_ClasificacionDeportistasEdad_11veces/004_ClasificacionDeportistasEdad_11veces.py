import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("CLASIFICACION DE DEPORTISTAS POR EDAD")

for i in range(11):
	edad = int(input("Ingrese la edad del deportista # {:d}, en años: ".format(i+1)))

	if edad <= 14:
		print("La categoría del deportista es PREJUVENIL")
	elif edad <= 18:
		print("La categoría del deportista es JUVENIL")
	else:
		print("La categoría del deportista es MAYORES")
	print("-"*47)

print()