#4.	La compañía de luz y sombras (CLS) requiere determinar el pago 
# que debe realizar una persona por el consumo de energía eléctrica, 
# la cual se mide en kilowatts (KW). 
# Realice un diagrama de flujo y pseudocódigo que representen el algoritmo que permita determinar ese pago.

#datos de entrada
consumo_energia = float(input("Ingrese los kw consumidos: "))
tarifa_energia = float(input("Ingrese el precio por kw: "))

#Calcular el pago por la energia
pago_energia = consumo_energia * tarifa_energia

#mostrar el pago de energia en pantalla
print(f"El total a pagar por los: {consumo_energia}kw es: ${pago_energia}")