import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("JUEGO DE MULTIPLOS Y TERMINADOS EN ****")

cantidad = int(input("Ingrese el numero maximo del juego: "))
disparador = int(input("Ingrese el numero clave o disparador\n\tEste el numero del cual seran multiplos y se termina que seran reemplazados por la palabra\n\tNumero disparador: "))
palabra = input("Ingrese la palabra a que reemplazara el numero clave: ")

for i in range(1, cantidad+1, 1):
	if (i%disparador == 0) or (i%10 == disparador):
		print("->",palabra," => (",i,")")
	else:
		print("->",i)

print()