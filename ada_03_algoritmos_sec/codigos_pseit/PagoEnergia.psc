Algoritmo PagoEnergia
	//Definir las varibles a usar
	Definir consumo_energia, tarifa_energia, pago_energia Como Real
	//Datos de entrada, se necesitan el consumo de energia y la tarifa energia, todo eso en kw
	Escribir 'Ingrese los kw consumidos:'
	Leer consumo_energia
	Escribir 'Ingrese el precio por kw:'
	Leer tarifa_energia
	//Calcular el pago por la energia que consumo de energia por la tarifa y almacenarlo
	pago_energia = consumo_energia * tarifa_energia
	//Mostrar el pago de energia en pantalla
	Escribir 'El total a pagar por el consumo de: ', consumo_energia, ' kw, es de: $', pago_energia
FinAlgoritmo
