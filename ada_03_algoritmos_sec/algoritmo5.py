#5.	Realice un diagrama de flujo y pseudocódigo 
# que representen el algoritmo para determinar 
# cuanto pagará finalmente una persona por un artículo equis, 
# considerando que tiene un descuento de 20%, 
# y debe pagar 15% de IVA (debe mostrar el precio con descuento y el precio final).


#dato de entrada
precio_articulo = float(input("Ingrese el precio del articulo: "))

#proceso para calcular el precio final del producto
descuento_articulo = precio_articulo*.20
precio_articulo_descuento = precio_articulo - descuento_articulo
iva_articulo = precio_articulo_descuento * .15
precio_final_articulo = precio_articulo_descuento + iva_articulo

#imprimir el precio final en pantalla 
print(f"El precio final del producto con precio incial: ${precio_articulo} es: ${precio_articulo_descuento}")