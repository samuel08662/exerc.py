# Função para gerar números inteiros no intervalo
def gerar_intervalo(num1, num2):
    # Verifica qual é o menor e o maior número
    inicio = min(num1, num2)
    fim = max(num1, num2)

    # Gera e imprime os números no intervalo
    for i in range(inicio + 1, fim):
        print(i)

# Solicita a entrada dos números
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Chama a função com os números fornecidos
gerar_intervalo(numero1, numero2)
