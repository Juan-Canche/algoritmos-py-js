#2.	Se requiere determinar el tiempo que tarda una persona 
# en llegar de una ciudad a otra en bicicleta, 
# considerando que lleva una velocidad constante. 
# Realice un diagrama de flujo y pseudocódigo que representen el algoritmo para tal fin.


#Datos de entrada
distancia_ciudades = float(input("Ingrese la distancia de una ciudad a otra en kilometros: "))
velocidad_bicicleta = float(input("ingrese la velociadad de la bicicleta en kilometros hora: "))

#calcular el tiempo de viaje que es distancia entre la velocidad de la bicicleta
tiempo_viaje = distancia_ciudades / velocidad_bicicleta

#Imprimir el resultado en horas
print(f"El tiempo para llegar a la otra ciudad en horas es: {tiempo_viaje}")

