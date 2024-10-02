#receba o primeiro numero do usuario

numero1 = float(input("digite o primeiro numero: "))

#receba o segundo numero do usuario
numero2 = float(input("digite o segundo numero: "))

#receba o tipo de operacao desejada
operacao = input("digite a operacao desejada (soma ou subtracao): ").strip().lower()

#realiza o calculo com base na operacao escolhida
if operacao == 'soma':
    resultado = numero1 + numero2
    print(f"o resultado da soma e: {resultado}")
elif operacao == 'subtracao':
    resultado = numero1 - numero2
    print(f"o resultado da subtracao e: {resultado}")
else:
    print("operacao invalida. por favor, digite 'soma' ou 'subtracao'.")   
