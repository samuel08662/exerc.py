#solicita ao usuario o salario atual do funcionario
salario_atual = float(input("digite o salario atual do funcionario: "))

#calcula o aumento de 20%
aumento = salario_atual * 0.25

#calcula o novo salario
novo_salario = salario_atual + aumento

#exibe o novo salario 
print(f"novo salario apos o aumento de 25%: R${novo_salario:.2f}")