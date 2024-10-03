nota_uno = float(input("Ingrese la nota 1: "))
nota_dos = float(input("Ingrese la nota 2: "))
nota_tres = float(input("Ingrese la nota 3: "))
nota_cuatro = float(input("Ingrese la nota 4: "))

promedio_notas = (nota_uno + nota_dos + nota_tres + nota_cuatro) / 4

print(f"El promedio general de las pruebas de desempeño: {promedio_notas}")


#otra forma menos repetitiva
promedio_pruebas = 0

for i in range(1, 5):
    nota = float(input(f"ingrese la nota {i}: "))
    promedio_pruebas += nota / 4
    
print(f"Promedio de las notas de las pruebas de desempeño: {promedio_pruebas}")