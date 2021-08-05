Proceso Ejercicio004_CategoriaDeportistaEdad_11veces
	
	Definir edad Como Entero;
	Definir i como Entero;	
	
	Para i<-1 Hasta 11 Con Paso 1 Hacer
		Escribir "Ingrese la edad del deportista #", (i), ": ";
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
		Escribir "------------------------------------------------------";
		
	FinPara
	
FinProceso