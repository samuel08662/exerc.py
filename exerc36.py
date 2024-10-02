# Pergunta ao usuário um número
numero = int(input("Digite um número de 1 a 7 para saber o dia da semana (1-Domingo, 2-Segunda, ...): "))

# Exibe o dia correspondente
if numero == 1:
    dia = "Domingo"
elif numero == 2:
    dia = "Segunda"
elif numero == 3:
    dia = "Terça"
elif numero == 4:
    dia = "Quarta"
elif numero == 5:
    dia = "Quinta"
elif numero == 6:
    dia = "Sexta"
elif numero == 7:
    dia = "Sábado"
else:
    dia = "Valor inválido"

# Exibe o resultado
print(dia)
