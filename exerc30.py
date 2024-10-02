def calculadora():
  print("Bem-vindo à Calculadora!")

  # Recebe os dois números do usuário
  try:
      num1 = float(input("Digite o primeiro número: "))
      num2 = float(input("Digite o segundo número: "))
  except ValueError:
      print("Por favor, digite valores numéricos válidos.")
      return

  # Recebe o tipo de operação desejada
  operacao = input("Digite a operação desejada (Soma, Subtração, Multiplicação, Divisão): ").strip().lower()

  # Realiza o cálculo de acordo com a operação desejada
  if operacao == 'soma':
      resultado = num1 + num2
      print(f"O resultado da soma é: {resultado}")
  elif operacao == 'subtração':
      resultado = num1 - num2
      print(f"O resultado da subtração é: {resultado}")
  elif operacao == 'multiplicação':
      resultado = num1 * num2
      print(f"O resultado da multiplicação é: {resultado}")
  elif operacao == 'divisão':
      if num2 == 0:
          print("Erro: Divisão por zero não é permitida.")
      else:
          resultado = num1 / num2
          print(f"O resultado da divisão é: {resultado}")
  else:
      print("Operação inválida. Por favor, escolha entre Soma, Subtração, Multiplicação e Divisão.")

# Executa a função calculadora
calculadora()

