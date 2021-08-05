import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
	print("WINDOWS => ", end="")
else:
	os.system("clear")
	print("UNIX => ", end="")
print("Hola a todos")

print()