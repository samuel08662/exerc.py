def main():
  # Cria uma lista vazia para armazenar os números
  numeros = []

  # Recebe 10 números do usuário
  for i in range(10):
      while True:
          try:
              # Tenta converter a entrada para um número
              numero = float(input(f"Digite o {i+1}º número: "))
              numeros.append(numero)
              break  # Sai do loop se a entrada for válida
          except ValueError:
              print("Entrada inválida. Por favor, digite um número.")

  # Inicializa as variáveis para o maior e menor número
  maior_numero = numeros[0]
  menor_numero = numeros[0]

  # Percorre a lista para encontrar o maior e menor número
  for numero in numeros:
      if numero > maior_numero:
          maior_numero = numero
      if numero < menor_numero:
          menor_numero = numero

  # Exibe o maior e o menor número
  print(f"O maior número é: {maior_numero}")
  print(f"O menor número é: {menor_numero}")

# Chama a função principal
if __name__ == "__main__":
  main()
