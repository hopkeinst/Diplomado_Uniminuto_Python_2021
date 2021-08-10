import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("TABLA DE MULTIPLICAR")
print("El programa le pedirá los 2 valores para calcular la tabla de multiplicar. Si desea salir ingrese '0' en alguna de las 2 opciones de ingreso de datos.\n")

f1 = None
f2 = None

while (f1 != 0) and (f2 != 0):
	f1 = None
	f2 = None
	while(f1 == None):
		try:
			f1 = int(input("Ingrese el número entero del cual desea conocer su tabla de multiplicar: "))
		except ValueError:
			print("-- ERROR -- Ingresaste un valor no entero.\nIntente de nuevo.\n")
	if f1 != 0:
		while(f2 == None):
			try:
				f2 = int(input("Ingrese el segundo factor hasta donde quiere llegar la multiplicación: "))
			except ValueError:
				print("-- ERROR -- Ingresaste un valor no entero.\nIntente de nuevo.\n")
		for c in range(f2):
			r = f1*(c+1)
			print("\t{:d} * {:d} = {:d}".format(f1, (c+1), r))
	print()

print("Fin del programa")
 
print()