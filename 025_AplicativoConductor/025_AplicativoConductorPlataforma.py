import os
import sys
import math as m

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("APLICATIVO PARA LA PARTE DEL CONDUCTOR DE UNA PLATAFORMA DE SERVICIO DE TRANSPORTE")

aporte = 0

while aporte <= 0:
	try:
		aporte = int(input("Ingrese el monto que va a dar inicialmente a la plataforma para habilitarlo: $"))
		if aporte <=0 :
			print("-- ERROR -- Ingresaste un valor de dinero menor o igual a 1 !!!\nInténtelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no numérico.\nInténtelo de nuevo.\n")

aporte_inicial = aporte
cnt_viajes = 0
dinero_recogido = 0
print("## Inicio de recaudo de dinero de viajes ##")
while aporte > 0:
	cnt_viajes += 1
	dinero = 0
	while dinero <= 0:
		try:
			dinero = int(input("-> Ingrese dinero recogido en el {:d} viaje: $".format(cnt_viajes)))
			if dinero <= 0:
				print("-- ERROR -- Ingresaste un valor menor o igual que CERO, y no es posible.\nInténtelo de nuevo.\n")
		except ValueError:
			print("-- ERROR -- Ingresaste un dato no numérico.\nInténtelo de nuevo.\n")
	dinero_recogido += dinero
	aporte -= (dinero*0.1)

print("\nYA LLEGASTE AL APORTE INICIAL !!!")
print("Cantidad de viajes realizados por el conductor: {:d}".format(cnt_viajes))
print("Dinero recaudado por el conductor: ${:d}".format(dinero_recogido))
print("Dinero aportado a la plataforma por el conductor: ${:d}".format(aporte_inicial))
if aporte < 0:
	print(" -- Quedaste debiendo dinero a la plataforma -> ${:d}".format(int(aporte)))
print("Dinero ganado por el conductor: ${:d} WIIII !!!".format(int(dinero_recogido+aporte-aporte_inicial)))

print()