import os
import sys

def limpiar_pantalla():
	sistema_operativo = sys.platform
	if sistema_operativo.startswith('win'):
		os.system("cls")
	else:
		os.system("clear")

def saludo(nPerson):
	print("Hola ",nPerson," ¿Cómo estás?", sep="")

limpiar_pantalla()
print("FUNCIONES - INTRO")
nombre = input("Ingresa tu nombre: ")
saludo(nombre)

print()