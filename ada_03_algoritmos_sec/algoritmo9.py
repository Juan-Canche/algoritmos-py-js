#9.	Realice el diagrama de flujo y pseudocódigo que representen el algoritmo para 
# determinar el promedio que obtendrá un alumno considerando que realiza tres exámenes, 
# de los cuales el primero y el segundo tienen una ponderación de 25%, mientras que el tercero de 50%.

#Datos de entrada, se piden las tres notas obtenidas
nota_examen_uno = float(input("Ingrese la nota del primer examen: "))
nota_examen_dos = float(input("Ingrese la nota del segundo examen: "))
nota_examen_tres = float(input("Ingrese la nota del tercer examen: "))

#Calcular el promedio multiplicando cada uno por su porcentaje y luego sumar
promedio_examenes = (nota_examen_uno*.25) + (nota_examen_dos*.25) + (nota_examen_tres*.50)

#Imprimir el promedio en la pantalla
print(f"El promedio de los examenes es: {promedio_examenes}")
