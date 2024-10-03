Algoritmo AhorroAnual
	//Definir las varibles
	Definir sueldo Como Real
	Definir ahorro_semanal Como Real
	Definir ahorro_mensual Como Real
	Definir ahorro_anual Como Real
	//Dato de entrada, se necesita el sueldo 
	Escribir "Ingrese el sueldo semanal:"
	Leer sueldo
	//Calcular el ahorro semanal es el 15% de su sueldo, mensual y anual
	ahorro_semanal = sueldo * .15
	ahorro_mensual = ahorro_semanal * 4
	ahorro_anual = ahorro_mensual * 12
	//Mostrar en pantalla en ahorro anual
	Escribir "El ahorro anual es de: $", ahorro_anual
	
FinAlgoritmo
