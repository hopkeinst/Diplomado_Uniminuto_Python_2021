import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("TELETON")

meta = int(input("Ingrese la meta que se quiere alcanzar en el teleton: $"))
cnt_donaciones = 0
donaciones = 0

while donaciones < meta:
	cnt_donaciones += 1
	donacion = int(input("\tIngrese la {:d} donacion -> $".format(cnt_donaciones)))
	donaciones += donacion

print("¡GENIAL! Hemos alcanzado la meta de ${:d} después de {:d} donaciones".format(donaciones, cnt_donaciones))

print()