import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("LISTAS - TRABAJO CON 2 LISTAS")
print("Se van a trabajar 2 listas para guardar datos de productos y cantidades.")

print("\nVas a ingresar los productos a medida que se le solicite.\nSi no desea ingresar más productos ingrese 'NO' cuando se le solicite el producto.\n")

productos = []
p = ""
while p != "no":
	p = input("-> Producto: ")
	if p.lower() != "no":
		productos.append(p)

cantidades = []
print("\nAhora vas a ingresar las cantidades para cada producto")
for i in productos:
	cnt = None
	while cnt == None:
		try:
			str_input = input("Ingrese la cantidad para el producto {:s}: ".format(i))
			cnt = int(str_input)
		except ValueError:
			try:
				cnt = float(str_input)
			except ValueError:
				print("-- ERROR -- Ingresaste un valor no numérico (entero o con decimales).\n\tInténtelo de nuevo.\n")
				cnt = None
	cantidades.append(cnt)

print()
for i in range(len(productos)):
	print("El producto {:s} tiene {} existencias".format(productos[i], cantidades[i]))


print("\nMÍNIMAS EXISTENCIAS")
minimo = 0
while minimo <= 0:
	try:
		minimo = int(input("Ingrese la cantidad mínima para todos los productos: "))
		if minimo <= 0:
			print("-- ERROR -- Ingresaste un valor menor o igual que cero.\n\tInténtelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un valor dato no numérico (entero o con decimales).\n\tInténtelo de nuevo.\n")

for i in range(len(productos)):
	if cantidades[i] <= minimo:
		print("El producto {:s} debe revisarse porque tiene menos de {:d} productos (actualmente {} cantidad).".format(productos[i], minimo, cantidades[i]))

print()