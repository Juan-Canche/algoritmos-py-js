from math import pi as PI

#area de una circuferencia

radio = float(input("Ingrese el radio de la circunferencia: "))

area_circunferencia = round(PI * radio**2,3)

print(f"El area de la circunferencia es: {area_circunferencia}")