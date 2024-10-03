#calcular el area en forma de cono de helado
from math import pi as PI

r = float(input("Ingrese el valor de r: "))
h = float(input("Ingrese el valor de h: "))

area_media_circunferencia = (PI * (r*r)) * 0.5
area_triangulo_rectangulo = ((h*h - r*r)**0.5)* r / 2
area_triangulo = 2 * area_triangulo_rectangulo

area_total = round(area_triangulo + area_media_circunferencia, 3)

print(f"Area media circuferencia: {area_media_circunferencia}")
print(f"Area del triangulo rectangulo: {area_triangulo_rectangulo}")
print(f"El area de la figura es: {area_total}")