def main():
    # Solicita o valor da base e do expoente ao usuário
    base = int(input("Digite o valor da base: "))
    expoente = int(input("Digite o valor do expoente: "))
    
    # Calcula a potência da base elevada ao expoente
    if expoente == 0:
        resultado = 1
    elif expoente == 1:
        resultado = base
    elif expoente == 2:
        resultado = base * base
    elif expoente == 3:
        resultado = base * base * base
    elif expoente == 4:
        resultado = base * base * base * base
    elif expoente == 5:
        resultado = base * base * base * base * base
    elif expoente == 6:
        resultado = base * base * base * base * base * base
    elif expoente == 7:
        resultado = base * base * base * base * base * base * base
    elif expoente == 8:
        resultado = base * base * base * base * base * base * base * base
    elif expoente == 9:
        resultado = base * base * base * base * base * base * base * base * base
    else:
        resultado = base ** expoente
    
    # Exibe o resultado
    print(f"O resultado de {base} elevado a {expoente} é: {resultado}")

# Executa a função principal
if __name__ == "__main__":
    main()
