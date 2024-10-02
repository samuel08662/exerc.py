def obter_nota_valida():
  while True:
      try:
          # Solicita a nota ao usuário
          nota = float(input("Digite uma nota entre 0 e 10: "))

          # Verifica se a nota está dentro do intervalo válido
          if 0 <= nota <= 10:
              print("Nota válida recebida:", nota)
              return nota
          else:
              print("Nota inválida! A nota deve estar entre 0 e 10.")

      except ValueError:
          print("Entrada inválida! Por favor, insira um número.")

# Chama a função para obter a nota válida
obter_nota_valida()
