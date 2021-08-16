import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("CAJERO ELECTRÓNICO - ATM\n")

opc = 1

while opc > 0:
	print("INICIO DE LA TRANSACCIÓN\n")
	try:
		dinero_solicitado = int(input("Ingrese la cantidad de dinero solicitado al cajero (multiplos de 10.000): $"))
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no numérico.\nEl cajero terminará la transacción.\n")
		print()
		exit()

	b_50 = 0
	b_20 = 0
	b_10 = 0
	dinero_faltante = dinero_solicitado

	if dinero_solicitado >= 1000000:
		print("-- ERROR -- Solicitaste más dinero del que puede despachar este cajero.\nEl cajero terminará la transacción.\n")
		print()
		exit()
	elif dinero_solicitado < 10000:
		print("-- ERROR -- Solicitaste menos de la cantidad de dinero mínima para despachar.\nEl cajero terminará la transacción.\n")
		print()
		exit()
	elif (dinero_solicitado%10000) != 0:
		print("-- ERROR -- Solicitaste una cantidad de dinero no múltiplo de 10.000 y no se puede entregar.\nEl cajero terminará la transacción.\n")
		print()
		exit()
	else:
		while dinero_faltante>0:
			while dinero_faltante >= 50000:
				b_50 += 1
				dinero_faltante -= 50000
			while dinero_faltante >= 20000:
				b_20 += 1
				dinero_faltante -= 20000
			while dinero_faltante >= 10000:
				b_10 += 1
				dinero_faltante -= 10000

	print("\nTODO TU DINERO FUE ENTREGADO !!!")
	print("Revisa la salida del dinero, debes tener ${:d} de la siguiente manera:".format(dinero_solicitado))
	if b_50 == 1:
		print("\t- 1 billete de $50.000")
	elif b_50 > 1:
		print("\t- {:d} billetes de $50.000".format(b_50))
	if b_20 == 1:
		print("\t- 1 billete de $20.000")
	elif b_20 > 1:
		print("\t- {:d} billetes de $20.000".format(b_20))
	if b_10 == 1:
		print("\t- 1 billete de $10.000")
	elif b_10 > 1:
		print("\t- {:d} billetes de $10.000".format(b_10))

	print("\nGracias por usar nuestros servicios\n\nFinaliza la transacción\n")

	print("-> Para INICIAR un nuevo retiro ingrese cualquier tecla seguido de 'Enter' o para SALIR presione solamente 'Enter'")
	opc = len(input(""))

print("\nFIN DEL CAJERO")

print()