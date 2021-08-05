import os
import sys
import math as m

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("PRUEBA COMPUERTA AND EN PYTHON => c = a AND b")

valores = [True, False]

print()
print("-"*25)
print("|"+"{:^7s}".format("a")+"|"+"{:^7s}".format("b")+"|"+"{:^7s}".format("c")+"|")
print("-"*25)

for v in valores:
	for w in valores:
		print("|"+"{:^7s}".format(str(v))+"|"+"{:^7s}".format(str(w))+"|"+"{:^7s}".format(str(v and w))+"|")
		print("-"*25)

print()