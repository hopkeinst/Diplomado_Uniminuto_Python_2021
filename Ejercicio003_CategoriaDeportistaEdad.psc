Proceso Ejercicio003_CategoriaDeportistaEdad
	
	Definir edad Como Entero;
	Escribir "Ingrese la edad del deportista: ";
	Leer edad;
	
	Si edad <= 14 Entonces
		Escribir "El deportista pertenece a la categoría PREJUVENIL";
	SiNo
		Si edad <= 18 Entonces
			Escribir "El deportista pertenece a la categoría JUVENIL";
		SiNo
			Escribir "El deportista pertenece a la categoría MAYORES";
		FinSi
	FinSi
	
FinProceso
