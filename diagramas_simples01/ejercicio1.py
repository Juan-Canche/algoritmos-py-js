precio_total = 0

producto = input("Tipo de producto 1: ")
cantidad = int(input("Ingrese la cantidad de producto 1: "))
precio_producto = float(input("Ingrese el precio del producto 1: "))

precio_total = cantidad * precio_producto


print(f"El precio del producto de tipo: {producto}, es: ${precio_producto}")
print(f"El precio total es: ${precio_total}")