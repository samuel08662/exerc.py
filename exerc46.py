def gerar_tabuada():
  while True:
      try:
          # Solicita um número ao usuário
          numero = int(input("Digite um número entre 1 e 10 para ver a tabuada: "))

          # Verifica se o número está dentro do intervalo válido
          if 1 <= numero <= 10:
              break  # Sai do loop se o número for válido
          else:
              print("Número inválido! O número deve estar entre 1 e 10.")

      except ValueError:
          print("Entrada inválida! Por favor, insira um número inteiro.")

  # Exibe a tabuada para o número informado
  print(f"TABUADA de {numero}:")
  for i in range(1, 11):
      resultado = numero * i
      print(f"{numero} X {i} = {resultado}")

# Chama a função para gerar a tabuada
gerar_tabuada()
