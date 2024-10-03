Algoritmo PagoHuesped
	//Definir las varibles
	Definir total_dias, costo_dia_hotel, pago_huesped Como Real
	//Datos de entrada, se necesita el total de dias que se hospeda un huesped y el costo por dia del hotel
	Escribir 'Ingrese el numero de dias que se hospedo el huesped:'
	Leer total_dias
	Escribir 'Ingrese el costo del hospedaje por dia del hotel:'
	Leer costo_dia_hotel
	//Calcular el pago que debe hacer el huesped
	pago_huesped = total_dias * costo_dia_hotel
	//Mostrar en pantalla lo que debe pagar el huesped
	Escribir 'El costo a pagar por el huesped es: $', pago_huesped
FinAlgoritmo
