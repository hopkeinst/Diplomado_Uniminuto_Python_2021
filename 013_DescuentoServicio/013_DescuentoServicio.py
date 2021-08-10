import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("DESCUENTO DE 10 SERVICIOS")

for i in range(10):
	valor_servicio = int(input("Ingrese el valor del {:d} servicio: $".format(i+1)))
	if valor_servicio > 200000:
		print("\t --> Aplica descuento del 15%")
		valor_servicio *= 0.85
	else:
		print("\t --> Aplica descuento del 10%")
		valor_servicio *= 0.9
	print("\tValor a pagar del servicio ${:.0f}".format(valor_servicio))

print()