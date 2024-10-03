Algoritmo TiempoViaje
	//Definir lo tipos de datos
	Definir distancia_ciudades, velocidad_bicicleta, tiempo_viaje Como Real
	//Datos de entrada se necesita la distancia entre las ciudades y la velocidad constante de la bicicleta
	Escribir "Ingrese la distancia de una ciudad a otra en kilometros:"
	Leer distancia_ciudades
	Escribir "Ingrese la velocidad de la bicicleta en kilometros hora:"
	Leer velocidad_bicicleta
	//Calcular el tiempo de viaje que es la distancia de las ciudades entre la velocidad de la bicicleta
	tiempo_viaje = distancia_ciudades / velocidad_bicicleta
	//Mostrar en pantalla el resultado de tiempo_viaje en horas
	Escribir "El tiempo para llegar a la otra ciudad en horas es: ", tiempo_viaje
FinAlgoritmo
