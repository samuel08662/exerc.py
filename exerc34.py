# Pergunta ao usuário a altura
altura = float(input("Digite sua altura em metros: "))

# Pergunta ao usuário o sexo
sexo = input("Digite o sexo (H para Homens e M para Mulheres): ").strip().upper()

# Calcula o peso ideal
if sexo == 'H':
    peso_ideal = (72.7 * altura) - 58
elif sexo == 'M':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = None
    print("Sexo inválido. Por favor, digite 'H' ou 'M'.")

# Exibe o resultado se o sexo for válido
if peso_ideal is not None:
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
