#receba um numero inteiro do usuario
numero = int(input("digite um numero inteiro: "))

#verefica se o numero e multiplo de 5 
if numero % 5 == 0:
    print(f"o numero {numero} e multiplo de 5. ")
else:   
    print(f"o numero {numero} nao e multiplo de 5. ")