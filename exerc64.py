# Solicita ao usuário que insira uma palavra
palavra = input("Digite uma palavra: ")

# Cria uma lista vazia para armazenar as consoantes
consoantes = []

# Define uma string contendo todas as consoantes
consoantes_str = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

# Itera sobre cada caractere da palavra
for c in palavra:
    # Verifica se o caractere é uma consoante
    if c in consoantes_str:
        consoantes.append(c)

# Exibe a lista de consoantes
print("Consoantes encontradas:", consoantes)
