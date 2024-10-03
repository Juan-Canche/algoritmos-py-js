#3.	Se requiere determinar el costo que tendrá 
# realizar una llamada telefónica con base en el tiempo que dura la llamada 
# y en el costo por minuto. 
# Realice un diagrama de flujo y pseudocódigo que representen el algoritmo para tal fin.

#Datos de entrada
tiempo_llamada = float(input("Ingrese el tiempo de la llamada en minutos: "))
costo_minuto = float(input("Ingrese el costo por minuto de la llamada: "))

#calcular costo de la llamada que es multiplicar tiempo de la llamada por el costo
costo_llamada = tiempo_llamada * costo_minuto

#Imprimir en pantalla el costo de la llamada
print(f"El costo de la llamda es: ${costo_llamada}")
