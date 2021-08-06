import os
import sys
import math as m

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("CONTAR CANTIDAD DE NUMEROS PARES E IMPARES")

cnt_pares = 0
cnt_impares = 0

n_numeros = int(input("Ingrese la cantidad total de numeros: "))

for i in range(n_numeros):
	numero = int(input("\tIngrese el numero: "))
	if numero%2 == 0:
		cnt_pares += 1
	else:
		cnt_impares += 1

print("Cantidad de numeros pares: {:d}".format(cnt_pares))
print("Cantidad de numeros impares: {:d}".format(cnt_impares))

print()