# Pergunta ao usuário os números
numero_inteiro1 = int(input("Digite o primeiro número inteiro: "))
numero_inteiro2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite um número real: "))

# Calcula os resultados
produto = (2 * numero_inteiro1) * (numero_inteiro2 / 2)
soma = (3 * numero_inteiro1) + numero_inteiro2
cubo = numero_inteiro2 ** 3

# Exibe os resultados
print(f"Produto do dobro do primeiro com metade do segundo: {produto}")
print(f"Soma do triplo do primeiro com o segundo: {soma}")
print(f"Segundo elevado ao cubo: {cubo}")
