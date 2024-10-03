#7.	Una empresa desea determinar el monto de un cheque 
# que debe proporcionar a uno de sus empleados 
# que tendrá que ir por equis número de días a la ciudad de Monterrey; 
# los gastos que cubre la empresa son: hotel, comida y 100.00 pesos diarios para otros gastos. 
# El monto debe estar desglosado para cada concepto. 
# Realice un diagrama de flujo y pseudocódigo que representen el algoritmo que determine el monto del cheque.

#datosde entrada
numero_dias = int(input("Ingrese el numero de días que ira el empleado a Monterrey: "))
precio_hotel_diario = float(input("Ingrese el precio del hotel por dia: "))
precio_comida_diario = float(input("Ingrese el gasto de comida por día: "))

#constante de gasto diario adicional
otros_gastos = 100.00

#Calcular los montos por separado
gasto_hotel = precio_hotel_diario * numero_dias
gasto_comida = precio_comida_diario * numero_dias
gasto_adicional = otros_gastos * numero_dias

#calcular el monto final sumando los gastos anteriores totales
monto_cheque = gasto_hotel + gasto_comida + gasto_adicional

#imprimir el monte del cheque en pantalla
print(f"\nEl monto del cheque es: ${monto_cheque}\n")
print(f"Desgloce de los gastos")
print(f"Hotel: ${gasto_hotel}")
print(f"Comida: ${gasto_comida}")
print(f"Otros gastos: ${gasto_adicional}")

