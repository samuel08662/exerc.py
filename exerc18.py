def inicio():
    deposito = float(input("Digite o valor do depósito: "))
    juros = float(input("Digite o valor dos juros: "))
    
    juros = juros / 100
    rendimento = deposito * juros
    vtotal = rendimento + deposito
    
    print(f"O seu rendimento foi de R${rendimento:.2f}.")
    print(f"E o valor total depois do rendimento foi de R${vtotal:.2f}.")

inicio()
