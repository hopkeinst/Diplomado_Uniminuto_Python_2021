Proceso Ejercicio003_CategoriaDeportistaEdad
	
	Definir edad Como Entero;
	Escribir "Ingrese la edad del deportista: ";
	Leer edad;
	
	Si edad <= 14 Entonces
		Escribir "El deportista pertenece a la categor�a PREJUVENIL";
	SiNo
		Si edad <= 18 Entonces
			Escribir "El deportista pertenece a la categor�a JUVENIL";
		SiNo
			Escribir "El deportista pertenece a la categor�a MAYORES";
		FinSi
	FinSi
	
FinProceso
