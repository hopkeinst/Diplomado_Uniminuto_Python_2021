import os
import sys

def limpiar_pantalla():
	sistema_operativo = sys.platform
	if sistema_operativo.startswith('win'):
		os.system("cls")
	else:
		os.system("clear")

def collatz(n, cnt):
	if (n%2) == 1:
		n = (3*n)+1
	else:
		n = n//2
	if n == 1:
		cnt += 1
	if cnt == 3:
		print(n)
		print("Fin de la serie")
		return None
	else:
		print(n, end=" -> ")
		collatz(n, cnt)

limpiar_pantalla()
print("CONJETURA COLLATZ")
print("La serie se termina después de llegar 3 veces a 1.")

n = 0
while n <= 0:
	try:
		n = int(input("Ingrese un número para recorrer la conjetura de Collatz (número natural): "))
		if n <= 0:
			print("-- ERROR -- Ingresaste un número menor o igual que cero.\nInténtelo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no numérico.\nInténtelo de nuevo.\n")

print()
if (n%2) == 0:
	print("Número inicial par")
else:
	print("Número inicial impar")
print(n, end=" -> ")
collatz(n, 0)

print()