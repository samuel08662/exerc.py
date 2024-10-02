def main():
  # Número de alunos e notas
  num_alunos = 4
  num_notas = 4

  # Criar uma matriz para armazenar os dados
  # Adicionaremos uma coluna extra para a média, então o tamanho das colunas será num_notas + 1
  matriz = [[0] * (num_notas + 1) for _ in range(num_alunos)]

  # Criar uma lista para armazenar os nomes dos alunos
  nomes_alunos = []

  # Receber os nomes dos alunos
  for i in range(num_alunos):
      nome = input(f"Digite o nome do aluno {i + 1}: ")
      nomes_alunos.append(nome)

      # Receber as notas dos alunos
      notas = []
      for j in range(num_notas):
          nota = float(input(f"Digite a nota {j + 1} do aluno {nome}: "))
          notas.append(nota)

      # Calcular a média
      media = sum(notas) / num_notas

      # Armazenar as notas e a média na matriz
      matriz[i] = notas + [media]

  # Exibir a matriz final com as médias
  print("\nMatriz com as notas e médias dos alunos:")
  for i, aluno in enumerate(nomes_alunos):
      print(f"Aluno: {aluno}")
      print(f"Notas: {matriz[i][:-1]}")
      print(f"Média: {matriz[i][-1]:.2f}")
      print()

if __name__ == "__main__":
  main()
