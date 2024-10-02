def main():
    # Solicita a base do triângulo ao usuário
    base = float(input("Digite a base do triângulo: "))
    
    # Solicita a altura do triângulo ao usuário
    altura = float(input("Digite a altura do triângulo: "))
    
    # Calcula a área do triângulo
    area = (base * altura) / 2
    
    # Exibe a área do triângulo
    print(f"A área do triângulo é: {area}")

# Executa a função principal
if __name__ == "__main__":
    main()
