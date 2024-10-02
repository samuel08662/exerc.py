def inicio():
    salario = float(input("Salário: "))
    percentual_de_aumento = float(input("Digite percentual de aumento: "))
    aumento = (salario * percentual_de_aumento) / 100
    novo_salario = salario + aumento
    print(f"O aumento foi de R${aumento:.2f}. Seu novo salário é de R${novo_salario:.2f}")

inicio()
