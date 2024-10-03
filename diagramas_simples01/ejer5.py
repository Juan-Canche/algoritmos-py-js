GALON = 3.785

litros_productor = float(input("Ingrese el numero de litros de leche: "))
precio_galon = float(input("Ingrese el precio del galon de leche: "))

total_galones = litros_productor / GALON
total_dinero = round(precio_galon * total_galones,3)

print(f"\nLitros proporcionados: {litros_productor}")
print(f"En galones equivale: {round(total_galones,3)}")
print(f"El total por los galones de leche es: {total_dinero}")