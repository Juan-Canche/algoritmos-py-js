#8.	Se desea calcular la potencia eléctrica de circuito de la siguiente figura. 
# Realice un diagrama de flujo y el pseudocódigo que representen el algoritmo para resolver el problema. 
# Considere que: P = V*I y V = R*I.

#mensaje inicial
print("Calcular la potencia electrica de un circuito\n")

#datos de entrada la resistencia y la corriente
r = float(input("ingrese el valor de la resistencia en ohmios: "))
i = float(input("Ingrese el valor de la corriente en amperios: "))

#calcular voltaje
v = r * i
#cacular potencia
p = v * i

#Mostrar en pantalla la potencia electrica
print(f"\nLa potencia electrica es: {p} vatios")
