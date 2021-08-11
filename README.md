# DIPLOMADO DE LENGUAJE DE PROGRAMACIÓN - PYTHON
# UNIMINUTO - SCOTIABANK COLPATRIA

En este repositorio están los códigos trabajados en las clases del diplomado de Lenguaje de Programación: Python dictado por la Corporación Universitaria Minuto de Dios *(UNIMINUTO)*. El sponsor o patrocinador de este diplomado es Scotiabank Colpatria. [Aquí puedes encontrar más información al respecto](https://www.uniminuto.edu/Convenio-Colpatria-UNIMINUTO).

El diplomado tiene un área de profundización *(python obviamente)* y unas horas en áreas transversales como Competencias Ciudadanas, Inglés, Emprendiemiento. El total son **360 horas** de las cuales 270 son en profundización y 90 en transversales.

El área de profundización es impartida por el ingeniero Llamas.

Como mencionaba, este repositorio tendrá los ejercicios desarrollados en la clase, pero de profundización. Tendrá mezcla de código y pseudocódigo *(desarrollado en [PSeInt](http://pseint.sourceforge.net/))*

***Comment:*** A medida que el tiempo lo permita iré actualizándolo, comentando sobre que trata cada código e incluso subiendo imágenes sobre los resultados.

Dudas, comentarios y demás al correo *hopkeinst@gmail.com*.

**Listado de códigos**

- [**000_HolaMundo:**](000_HolaMundo) Ejercicio básico de todo lenguaje de programación para escribir o imprimir en pantalla un mensaje que diga 'Hola Mundo'.

- [**001_HolaATodos:**](001_HolaATodos) Ejercicio básico de impresión. Aquí se incluye la posibilidad de limpiar la consola antes de mostrar cualquier cosa. En este caso se hace una diferenciación dependiendo si el sistema operativo es Windows o no, porque el comando entre Windows y UNIX es diferente. Este sirve de base para limpiar la pantalla del resto de códigos aquí colocados.

- [**002_VolumenCono:**](002_VolumenCono) Aquí se busca calcular el volumen de un cono y el área de su base. Se usa la librería *math* para usar el número ***PI*** y se compara frente al valor establecido de 3.1416 como la constante.

- [**003_ClasificacionDeportistasPorEdad:**](003_ClasificacionDeportistasPorEdad) Código que solicita la edad de un deportista y le dice a que categoría pertenece.

- [**004_ClasificacionDeportistasEdad_11veces:**](004_ClasificacionDeportistasEdad_11veces)

- [**005_PruebaCompuertaXOR:**](005_PruebaCompuertaXOR)

- [**006_PruebaCompuertaAND:**](006_PruebaCompuertaAND)

- [**007_PruebaCompuertaOR:**](007_PruebaCompuertaOR)

- [**008_JuegoMultiplosyTerminados:**](008_JuegoMultiplosyTerminados)

- [**009_CantidadEstudiantesPasaron:**](009_CantidadEstudiantesPasaron)

- [**010_ContarParesImpares:**](010_ContarParesImpares)

- [**011_AcumuladorEdadPersonas:**](011_AcumuladorEdadPersonas)

- [**012_AcumuladorContadorProductos:**](012_AcumuladorContadorProductos)

- [**013_DescuentoServicio:**](013_DescuentoServicio)

- [**014_Teleton:**](014_Teleton)

> ***WOW*** A partir de aquí procuraré usar manejo de errores en los inputs para asegurar que se ingrese un dato correcto, dentro del dominio o rango esperado, que si se va a ingresar un número sea un número y no un texto.
Esto lo haré revisando los datos ingresados y forzando mediante `while` que se cumplan y para los tipos de datos mediante `try-except`.

- [**015_PelotaRebotante:**](015_PelotaRebotante) En este código la idea es tener una pelota que rebota al pasar el tiempo. Se tiene una altura inicial desde donde se suelta, una altura a la cual se quiere llegar y el porcentaje que va disminuyendo de la altura en cada rebote. Al final muestra el proceso como va disminuyendo en cada rebote y el total de rebotes que tuvo que hacer para alcanzar o ser menor que la altura mínima ingresada.

- [**016_TablaDeMultiplicar:**](016_TablaDeMultiplicar) En este código la idea es ingresar el número al que queremos hallar su respectiva tabla de multiplicar, luego solicita otro número que es hasta donde llegará esta tabla de multiplicar; para proceder a mostrarla.

- [**017_TablaDeMultiplicarRepetitivo:**](017_TablaDeMultiplicarRepetitivo) Igual que el anterior, solo que se repite de manera cíclica pidiendo los 2 datos de entrada y mostrando la tabla de multiplicar respectiva. Si en algún momento se desea salir basta con ingresar un '0' en alguno de los 2 datos de entrada.

- [**018_NumeroPrimo:**](018_NumeroPrimo) Código para revisar si un número es primo o no. Se utiliza el concepto de número primo que solo es divisible entre 1 y el mismo número; por lo cual revisa desde el número 2 hasta el número anterior al que se desea revisar y busca si es divisible por alguno de estos. Si es así, cambia el valor de una bandera y rompe el ciclo repetitivo. Luego imprime la información dependiendo del valor de la bandera. Se le agrega la librería `time` para medir tiempo y luego contrastarlo contra los dos siguientes códigos y ver cual es más rápido.

- [**019_NumeroPrimoOptimizado:**](019_NumeroPrimoOptimizado) Realiza la misma labor del código anterior, solamente que optimiza el límite superior del ciclo de repetición. Aquí usamos un concepto matemático que dice que los divisores de un número van hasta la raíz cuadrada de este número *(claro, si existen estos divisores)*. Se usa y se compara los tiempos frente al código anterior y da un orden de 91 veces más rápido.

- [**020_NumeroPrimoOptimizadoWhile:**](020_NumeroPrimoOptimizadoWhile) Igual que los dos anteriores códigos, solo que se cambia el ciclo repetitivo `for` por un ciclo repetitivo `while` y usando la raíz cuadrada del número que se quiere revisar. Aquí se nota que es más rápido que el código 018; pero no tanto como el 019 *(esto debido al incremento hecho al final del `while` que viene optimizado en el `for`)*.

- [**021_numerosAmigos_teoria1:**](021_numerosAmigos_teoria1) Código para identificar si 2 números son números amigos. Dos números son amigos cuando la suma de sus divisores son igual al otro número. O sea, si tengo los números A y B, la suma de los divisores de A es igual a B y la suma de los divisores de B es igual a A.
