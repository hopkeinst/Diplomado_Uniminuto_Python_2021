import os
import sys

def limpiar_pantalla():
	sistema_operativo = sys.platform
	if sistema_operativo.startswith('win'):
		os.system("cls")
	else:
		os.system("clear")

def saludar():
	print("Hola, cómo estás?")

limpiar_pantalla()
print("FUNCIONES - INTRO")
print("")
saludar()

print()