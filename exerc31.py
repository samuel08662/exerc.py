# Pergunta ao usuário um número
numero = int(input("Digite um número: "))

# Exibe a tabuada do número até 10
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
