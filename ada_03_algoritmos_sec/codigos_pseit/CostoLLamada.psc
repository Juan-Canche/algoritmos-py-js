Algoritmo CostoLLamada
	//Definir las variables a usar
	Definir tiempo_llamada, costo_minuto, costo_llamada Como Real
	//Datos de entrada, se necesita el tiempo de la llamada y el costo por minuto
	Escribir 'Ingrese el tiempo de la llamada en minutos'
	Leer tiempo_llamada
	Escribir 'Ingrese el costo por minuto de la llamada'
	Leer costo_minuto
	//Calcular el costo de la llamada que es tiempo de la llamada por costo por minuto
	costo_llamada = tiempo_llamada * costo_minuto
	//Imprimir el resultado en la pantalla
	Escribir 'El costo de la llamada es: $', costo_llamada
FinAlgoritmo
