# Define a quantidade de alunos
num_alunos = int(input("Digite o número de alunos na sala: "))

# Cria uma lista para armazenar os nomes
nomes = []

# Lê os nomes dos alunos
for i in range(num_alunos):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nomes.append(nome)

# Exibe a lista de nomes
print("Lista de alunos:")
for nome in nomes:
    print(nome)
