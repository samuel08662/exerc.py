def inicio():
    salario = float(input("Digite o seu salário: "))
    
    aumento = (5 * salario) / 100
    imposto = (7 * salario) / 100
    salarionv = aumento + salario
    salarioruim = salario - imposto
    salariototal = salario + aumento + imposto
    
    print(f"Sua gratificação é de: R${aumento:.2f}")
    print(f"Seu valor de imposto é de: R${imposto:.2f}")
    print(f"Seu salário final é de: R${salariototal:.2f}")

inicio()
