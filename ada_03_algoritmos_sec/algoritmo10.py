#10 El hotel “Cama Arena” requiere determinar lo que le debe cobrar a un huésped 
# por su estancia en una de sus habitaciones. Considere que el hospedaje 
# puede realizarse por varios días y el costo es por día. 
# Realice un diagrama de flujo y pseudocódigo que representen el algoritmo para determinar ese cobro.

#Datos de entrada se pide el total de dias y el costo del hotel por dia
total_dias = int(input("Ingrese el numero de dias que se hospedo el huesped: "))
costo_dia_hotel = float(input("Ingrese el costo del hospedaje por dia del hotel: "))

#Calcular el pago por parte del huesped
pago_huesped = total_dias * costo_dia_hotel

#Imprimir el pago del huesped en pantalla 
print(f"El costo a pagar por el huesped es: {pago_huesped}")
