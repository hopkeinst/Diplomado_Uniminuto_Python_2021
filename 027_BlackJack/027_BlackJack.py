import os
import sys
import random as r

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("BLACKJACK")
print("Se tomará la carta AS como el 1 solamente.\n")

# Uso de lista
cartas = ["AS", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

print("-> Inicia el jugador")
opc = -1
cartas_jugador = []
cartas_jugador.append(cartas[r.randint(0, 12)])
valor_jugador = 0
if cartas_jugador[-1] in ["J", "Q", "K"]:
	valor_jugador += 10
elif cartas_jugador[-1] == "AS":
	valor_jugador += 1
else:
	valor_jugador += int(cartas_jugador[-1])
print("\tTu primera carta es {:s} (Acumulado: {:d})".format(cartas_jugador[-1], valor_jugador))

while (opc != 0) and (valor_jugador <= 21):
	try:
		opc = int(input("Quieres sacar otra carta? (1 -> Si, 0 -> No, plantarse): "))
		if (opc != 0) and (opc != 1):
			print("-- ERROR -- Ingresaste un valor no válido, inténtalo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no entero, inténtalo de nuevo.\n")

	if (opc == 1):
		cartas_jugador.append(cartas[r.randint(0, 12)])
		if cartas_jugador[-1] in ["J", "Q", "K"]:
			valor_jugador += 10
		elif cartas_jugador[-1] == "AS":
			valor_jugador += 1
		else:
			valor_jugador += int(cartas_jugador[-1])
		print("\tSe te dió la carta {:s} (Acumulado: {:d})".format(cartas_jugador[-1], valor_jugador))
		
if valor_jugador <= 21:
	print("\nAhora va la casa (CRUPIER)")
	cartas_crupier = []
	valor_crupier = 0
	opc = -1
	cartas_crupier.append(cartas[r.randint(0, 12)])
	if cartas_crupier[-1] in ["J", "Q", "K"]:
		valor_crupier += 10
	elif cartas_crupier[-1] == "AS":
		valor_crupier += 1
	else:
		valor_crupier += int(cartas_crupier[-1])
	print("\tPrimera carta Crupier es {:s} (Acumulado: {:d})".format(cartas_crupier[-1], valor_crupier))

	while (valor_crupier <= 16):
		cartas_crupier.append(cartas[r.randint(0, 12)])
		if cartas_crupier[-1] in ["J", "Q", "K"]:
			valor_crupier += 10
		elif cartas_crupier[-1] == "AS":
			valor_crupier += 1
		else:
			valor_crupier += int(cartas_crupier[-1])
		print("\tCrupier sacó la carta {:s} (Acumulado: {:d})".format(cartas_crupier[-1], valor_crupier))

	if valor_crupier > 21:
		print("GANASTE !!! La casa pierde por sacar más de 21.")
	elif valor_crupier >= valor_jugador:
		print("PERDISTE !!! La casa gana por tener un valor igual o mayor al tuyo.")
	else:
		print("GANASTE !!! Sacaste una puntuación mayor que la casa.")
	##
else:
	print("PERDISTE !!! Sacaste más de 21.")

print()