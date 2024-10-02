# Inicializa contadores para números pares e ímpares
contagem_pares = 0
contagem_impares = 0

# Loop para solicitar 10 números inteiros ao usuário
for i in range(10):
    while True:
        try:
            numero = int(input(f"Digite o número inteiro: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    # Verifica se o número é par ou ímpar e atualiza os contadores
    if numero % 2 == 0:
        contagem_pares += 1
    else:
        contagem_impares += 1

# Mostra os resultados
print(f"Quantidade de números pares: {contagem_pares}")
print(f"Quantidade de números ímpares: {contagem_impares}")