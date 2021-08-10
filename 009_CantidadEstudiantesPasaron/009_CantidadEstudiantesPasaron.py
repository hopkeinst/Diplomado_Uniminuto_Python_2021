import os
import sys

sistema_operativo = sys.platform
if sistema_operativo.startswith('win'):
	os.system("cls")
else:
	os.system("clear")

print("CANTIDAD DE ESTUDIANTES QUE APROBARON")

cnt_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

pasaron = 0

for i in range(cnt_estudiantes):
	nota = float(input("Ingrese la nota del estudiante # {:d}: ".format(i+1)))
	if nota >= 3.0:
		pasaron += 1

print("\nTotal de estudiantes: {:d}".format(cnt_estudiantes))
print("Cantidad de estudiantes que pasaron: {:d}".format(pasaron))
print("Cantidad de estudiantes que no pasaron: {:d}".format(cnt_estudiantes-pasaron))

print()
