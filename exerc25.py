def main():
    # Solicita um número ao usuário
    numero = int(input("Digite um número: "))
    
    # Calcula o quadrado e o cubo do número
    quadrado = numero * numero
    cubo = numero * numero * numero
    
    # Exibe o quadrado e o cubo do número
    print(f"O número ao quadrado é: {quadrado}")
    print(f"O número ao cubo é: {cubo}")

# Executa a função principal
if __name__ == "__main__":
    main()
