import os
import sys
import random as r

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("INTRODUCCIÓN A LAS LISTAS - EJERCICIOS CON LISTA")

l_a = []
for i in range(10):
	l_a.append(r.randint(0,9))

print("Lista inicial:",l_a)

print()
print("Elementos con índice par:",l_a[0::2])
print("Elementos con índice impar:",l_a[1::2])
print("Primer elemento de la lista:",l_a[0])
print("Último elemento de la lista:",l_a[-1])
print("Lista invertida:",l_a[::-1])

print()