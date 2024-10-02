# Inicializa uma lista para armazenar os números
numeros = []

# Loop para ler 5 números do usuário
for i in range(5):
    while True:
      try:
        numero = float(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
        break
      except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

# Calcula a soma e a média dos números
soma = sum(numeros)
media = soma / len(numeros)

# Exibe a soma e a média
print(f"Soma dos números: {soma}")
print(f"Média dos números: {media}")
