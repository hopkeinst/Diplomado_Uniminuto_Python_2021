import os
import sys
import math as m

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("PRUEBA COMPUERTA XOR EN PYTHON => c = a XOR b")

valores = [True, False]

print()
print("Usando ^")
print("-"*25)
print("|"+"{:^7s}".format("a")+"|"+"{:^7s}".format("b")+"|"+"{:^7s}".format("c")+"|")
print("-"*25)

for v in valores:
	for w in valores:
		print("|"+"{:^7s}".format(str(v))+"|"+"{:^7s}".format(str(w))+"|"+"{:^7s}".format(str(v^w))+"|")
		print("-"*25)

print()