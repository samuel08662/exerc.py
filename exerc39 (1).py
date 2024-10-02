def imprimir_quantidade(num):
  if num < 0 or num >= 1000:
      print("Número fora do intervalo permitido.")
      return

  centenas = num // 100
  dezenas = (num % 100) // 10
  unidades = num % 10

  resultado = []

  if centenas > 0:
      if centenas == 1:
          resultado.append("1 centena")
      else:
          resultado.append(f"{centenas} centenas")

  if dezenas > 0:
      if dezenas == 1:
          resultado.append("1 dezena")
      else:
          resultado.append(f"{dezenas} dezenas")

  if unidades > 0:
      if unidades == 1:
          resultado.append("1 unidade")
      else:
          resultado.append(f"{unidades} unidades")

  # Construindo a string final
  if len(resultado) == 1:
      print(resultado[0])
  elif len(resultado) == 2:
      print(f"{resultado[0]} e {resultado[1]}")
  else:
      print(f"{', '.join(resultado[:-1])} e {resultado[-1]}")

# Leitura do número
try:
  numero = int(input("Digite um número inteiro menor que 1000: "))
  imprimir_quantidade(numero)
except ValueError:
  print("Entrada inválida. Por favor, digite um número inteiro.")
