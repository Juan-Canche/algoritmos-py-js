PULGADA = 0.0254

tela_metros = float(input("Ingrese la tela en metros: "))

tela_pulgadas = round(tela_metros / PULGADA, 3)

print(f"Los metros de tela: {tela_metros} a puldadas es: {tela_pulgadas}")