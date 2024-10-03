Algoritmo MontoCheque
	//Definir las variables
	Definir numero_dias Como Real
	Definir precio_hotel_diario Como Real
	Definir precio_comida_diario Como Real
	Definir OTROS_GASTOS Como Real
	Definir gasto_hotel Como Real
	Definir gasto_comida Como Real
	Definir gasto_adicional Como Real
	Definir monto_cheque Como Real
	//Incializar el valor de otros gastos como constante
	OTROS_GASTOS = 100.00
	//Datos de entrada
	Escribir 'Ingrese el numero de días que irá el empleado a Monterrey:'
	Leer numero_dias
	Escribir 'Ingrese el precio del hotel por día:'
	Leer precio_hotel_diario
	Escribir 'Ingrese el gasto de comida por día:'
	Leer precio_comida_diario
	//Calcular los montos de manera individual
	gasto_hotel = precio_hotel_diario * numero_dias
	gasto_comida = precio_comida_diario * numero_dias
	gasto_adicional = OTROS_GASTOS * numero_dias
	monto_cheque = gasto_hotel + gasto_comida + gasto_adicional
	//Imprimir el monto del cheque en pantalla y desglosar los gastos
	Escribir 'El monto del cheque es: $', monto_cheque
	Escribir '-----Desgloce de los gastos------'
	Escribir 'Hotel: $', gasto_hotel
	Escribir 'Comida: $', gasto_comida
	Escribir 'Otros gastos: $', gasto_adicional
FinAlgoritmo
