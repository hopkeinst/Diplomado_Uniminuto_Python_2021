import os
import sys
import math as m

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("DISMINUCION ALTURA DE PELOTA QUE REBOTA")
print("Este programa le permitirá calcular cuantos saltos demora una pelota en cambiar su altura de rebote teniendo en cuenta la altura desde la cual se suelta, la altura a la cual quiere llegar y el porcentaje que disminuye después de cada salto.\n")

h_max = -0.01
while(h_max <= 0):
	try:
		h_max = float(input("Ingrese la altura desde la que se suelta la pelota (metros): "))
		if not(h_max > 0):
			print("-- ERROR -- Ingresaste una altura de cero o negativa no válida\nIntentelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un valor no numérico _ni entero ni flotante_.\nInténtelo de nuevo.\n")
h_min = m.inf
while(h_min > h_max):
	try:
		h_min = float(input("Ingrese la altura a la que quiere llegar con el rebote de la pelota (metros): "))
		if h_min > h_max:
			print("-- ERROR -- Ingresaste una altura mayor que la altura desde donde se suelta la pelota.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un valor no numérico _ni entero ni flotante_.\nInténtelo de nuevo.\n")
porcentaje = 0.0
while(porcentaje <= 0):
	try:
		porcentaje = float(input("Ingrese el porcentaje que quiere que disminuya en cada rebote la pelota (%)): "))
		if porcentaje <= 0:
			print("-- ERROR -- Ingresaste un porcentaje negativo o igual a cero y no es posible. Inténtelo de nuevo\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un valor no numérico _ni entero ni flotante_.\nInténtelo de nuevo.\n")
cnt_rebotes = 0
h_actual = h_max
while(h_actual >= h_min):
	cnt_rebotes += 1
	h_actual = h_actual-(h_actual*(porcentaje/100))
	print("\t-> La pelota tuvo su {:d} rebote y ahora alcanza la altura de {:.3f} metros".format(cnt_rebotes, h_actual))

print("\nLa pelota ya alcanzó una altura menor a {:.3f} metros, después de {:d} rebotes llegó hasta {:.3f} metros".format(h_min, cnt_rebotes, h_actual))

print()