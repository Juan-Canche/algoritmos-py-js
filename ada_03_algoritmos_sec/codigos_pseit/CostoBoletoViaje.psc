Algoritmo CostoBoletoViaje
	Definir kilometros_recorridos, costo_kilometro, costo_boleto Como Real
	// Datos de entrada, se necesitan los kilometros y el costo por kilometro
	Escribir 'Ingrese los kilometros recorridos:'
	Leer kilometros_recorridos
	Escribir 'Ingrese el costo por kilometro:'
	Leer costo_kilometro
	// Calcular el costo del boleto con los kilometros recorridos * costo del kilometro
	costo_boleto = kilometros_recorridos*costo_kilometro
	// Imprimir el costo del boleto en pantalla
	Escribir 'El total a pagar por el boleto es: $', costo_boleto
FinAlgoritmo
