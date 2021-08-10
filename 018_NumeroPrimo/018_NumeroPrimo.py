import os
import sys
import time # Para medir el tiempo de ejecucion probando con un numero primo, frente al codigo optimizado

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("NUMERO PRIMO")

n = 0
f_primo = True

while (n < 2):
	try: 
		n = int(input("Ingrese numero que quiera conocer si es o no primo (mayor que 2): "))
		if n < 2:
			print("-- ERROR -- El valor que ingresaste es menor que 2.\nInténtalo de nuevo.\n")
	except ValueError:
		print("-- ERROR -- Ingresaste un dato no numérico.\nInténtalo de nuevo.\n")

t_ini = time.time()
for i in range(2, n):
	if (n%i) == 0:
		f_primo = False
		break

if f_primo == True:
	print("El número {:d} SI es primo".format(n))
else:
	print("El número {:d} NO es primo".format(n))

print()
print("Tiempo de ejecución:",(time.time()-t_ini))
print()