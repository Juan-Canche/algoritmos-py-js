Algoritmo PrecioArticulo
	//Definir las varibles a usar
	Definir precio_articulo Como Real
	Definir descuento_articulo Como Real
	Definir precio_articulo_descuento Como Real
	Definir iva_articulo Como Real
	Definir precio_articulo_final Como Real
	//Datos de entrada, se necesita el precio del articulo
	Escribir 'Ingrese el precio articulo del ariticulo:'
	Leer precio_articulo
	//Realizar los calculos
	descuento_articulo = precio_articulo * .20
	precio_articulo_descuento = precio_articulo - descuento_articulo
	iva_articulo = precio_articulo_descuento * .15
	precio_articulo_final = precio_articulo_descuento + iva_articulo
	//Mostrar en pantalla el precio final, efectuado todos los calculos necesarios
	Escribir 'El precio final del producto con precio inicial: $', precio_articulo, ' es: $', precio_articulo_descuento
	
FinAlgoritmo
