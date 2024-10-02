def main():
    # Solicita o ano de nascimento ao usuário
    ano_nascimento = int(input("Digite o seu ano de nascimento: "))

    # Calcula o ano atual (assumido como 2024)
    ano_atual = 2024

    # Calcula a idade
    idade = ano_atual - ano_nascimento
    
    # Calcula a idade em meses, dias e semanas
    anos_em_meses = idade * 12
    anos_em_dias = idade * 365
    anos_em_semanas = idade * 52

    # Calcula a idade em 2019
    idade_em_2019 = 2019 - ano_nascimento

    # Exibe os resultados
    print(f"Sua idade é: {idade}")
    print(f"Sua idade em meses é: {anos_em_meses}")
    print(f"Sua idade em dias é: {anos_em_dias}")
    print(f"Sua idade em semanas é: {anos_em_semanas}")
    print(f"Sua idade em 2019 era: {idade_em_2019}")

# Executa a função principal
if __name__ == "__main__":
    main()
