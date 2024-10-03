horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
sueldo_hora = float(input("Ingrese el sueldo por hora: "))

sueldo_semanal = round(horas_trabajadas * sueldo_hora,3)

print(f"El sueldo semanal es: {sueldo_semanal}")