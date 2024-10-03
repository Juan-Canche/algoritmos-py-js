#1.	La compañía de autobuses “La curva loca” requiere 
# determinar el costo que tendrá el boleto de un viaje sencillo, 
# esto basado en los kilómetros por recorrer y en el costo por kilómetro. 
# Realice un diagrama de flujo y pseudocódigo que representen el algoritmo para tal fin.

#Mensaje inicial
print("Calcular costo de un boleto de un viaje")

#Datos de entrada
kilometros_recorridos = float(input("Ingrese los kilometros recorridos: "))
costo_kilometro = float(input("Ingrese el costo por kilometro. "))

#calcular el costo del boleto que es kilometros por costo
costo_boleto = kilometros_recorridos * costo_kilometro

#Mostrar el resultado en pantalla
print(f"El total a pagar por el boleto es: ${costo_boleto}")