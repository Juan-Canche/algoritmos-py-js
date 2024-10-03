Algoritmo PotenciaElectrica
	//Definir las variables
	Definir resistencia, corriente, voltaje, potencia Como Real
	//Datos de entrada la resistencia en ohmios y la corriente en amperios
	Escribir 'Ingrese el valor de la resistencia:'
	Leer resistencia
	Escribir 'Ingrese el valor de la corriente en amperios:'
	Leer corriente
	//Calcular voltaje
	voltaje = resistencia * corriente
	//calcular potencia 
	potencia = voltaje * corriente
	//Mostrar en pantallala potencia electrica 
	Escribir 'La potencia electrica es de: ', potencia, ' vatios'
FinAlgoritmo
