x_menor = -10
x_mayor = 10

print("CICLO FOR")
print("-"*14)
print("|  x  | f(x) |")
print("-"*14)
for x in range(-10, 10+1, 1):
	resultado = (x*x) - (2*x) + 1
	print("|{:^5.1f}|{:^6d}|".format(x, resultado))

print("-"*14)
print()

print("CICLO WHILE")
x = -10
while x <= 10:
	resultado = (x*x) - (2*x) + 1
	print(x,"=",resultado)
	x = x + 1