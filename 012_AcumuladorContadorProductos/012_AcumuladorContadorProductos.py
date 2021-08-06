import os
import sys
import math as m

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("COMPRA DE ARTICULOS")

dinero_maximo = int(input("Ingrese la cantidad de dinero maxima que tiene para comprar: $"))

total_compra = 0
cnt_productos = 0

precio = int(input("\tIngrese el precio del producto: $"))

while (total_compra + precio) <= dinero_maximo:
	total_compra += precio
	print("\t --> Ingrese producto al carrito de compra |-| Subtotal ${:d}".format(total_compra))
	cnt_productos += 1
	precio = int(input("\tIngrese el precio del producto: $"))

print("\tTotal dinero gastado en la compra ${:d}".format(total_compra))
print("Cantidad de productos comprados: {:d}".format(cnt_productos))

print()