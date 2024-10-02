def encontrar_maior_numero():
  maior_numero = None  # Inicializa a variável para armazenar o maior número

  for i in range(5):  # Loop para ler 5 números
      while True:
          try:
              # Solicita um número ao usuário
              numero = float(input(f"Digite o {i + 1}º número: "))
              break  # Sai do loop se a entrada for válida
          except ValueError:
              print("Entrada inválida! Por favor, insira um número válido.")

      # Atualiza o maior número se o número atual for maior
      if maior_numero is None or numero > maior_numero:
          maior_numero = numero

  # Exibe o maior número encontrado
  print("O maior número é:", maior_numero)

# Chama a função para encontrar o maior número
encontrar_maior_numero()
