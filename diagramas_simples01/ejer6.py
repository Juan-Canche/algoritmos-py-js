#distancia de dos puntos
print("Calcular la distancia de dos puntos \n")

print("Punto 1")
x_uno = float(input("Ingrese el valor de x de la primera coordenada: "))
y_uno = float(input("Ingrese el valor de y de la primera coordenada: "))

print("\nPunto 2")
x_dos = float(input("Ingrese el valor de x de la segunda coordenada: "))
y_dos = float(input("Ingrese el valor de y de la segunda coordenada: "))

distancia_puntos = round(((x_dos - x_uno)**2 + (y_dos - y_uno)**2)**0.5, 3)

print(f"\nLa distancia del punto ({x_uno},{x_dos}) a ({x_dos},{y_dos}) es: {distancia_puntos}")
