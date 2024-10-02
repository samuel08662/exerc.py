# Inicializa os contadores para cada intervalo
contagem_intervalo_0_25 = 0
contagem_intervalo_26_50 = 0
contagem_intervalo_51_75 = 0
contagem_intervalo_76_100 = 0

# Loop para leitura dos números
while True:
    try:
        # Lê um número do usuário
        numero = float(input("Digite um número positivo (ou um número negativo para encerrar): "))

        # Verifica se o número é negativo para encerrar o loop
        if numero < 0:
            break

        # Verifica em qual intervalo o número se encaixa e incrementa o contador correspondente
        if 0 <= numero <= 25:
            contagem_intervalo_0_25 += 1
        elif 26 <= numero <= 50:
            contagem_intervalo_26_50 += 1
        elif 51 <= numero <= 75:
            contagem_intervalo_51_75 += 1
        elif 76 <= numero <= 100:
            contagem_intervalo_76_100 += 1
        else:
            print("Número fora do intervalo considerado (0-100).")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

# Exibe os resultados
print(f"Números no intervalo [0-25]: {contagem_intervalo_0_25}")
print(f"Números no intervalo [26-50]: {contagem_intervalo_26_50}")
print(f"Números no intervalo [51-75]: {contagem_intervalo_51_75}")
print(f"Números no intervalo [76-100]: {contagem_intervalo_76_100}")

