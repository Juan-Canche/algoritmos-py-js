# 6. Realice un diagrama de flujo y pseudocódigo que representen el algoritmo para 
# determinar cuanto dinero ahorra una persona en un año 
# si considera que cada semana ahorra 15% de su sueldo 
# (considere cuatro semanas por mes y que no cambia el sueldo).

#dato de entrada
sueldo = float(input("Ingrese el sueldo semanal: "))

ahorro_semanal = sueldo * .15
ahorro_mensual = ahorro_semanal * 4
ahorro_anual = ahorro_mensual * 12

print(f"El ahorro anual es de: ${ahorro_anual}")