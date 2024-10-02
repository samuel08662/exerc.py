# Cria uma lista vazia para armazenar os números ímpares
impares = []

# Percorre os números de 1 até 100
for numero in range(1, 101):
    # Verifica se o número é ímpar
    if numero % 2 != 0:
        impares.append(numero)

# Exibe o vetor de números ímpares
print(impares)
