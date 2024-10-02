def numero_por_extenso(num):
  unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
  dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
  especiais = ["", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

  if 0 <= num <= 9:
      return unidades[num]
  elif 10 <= num <= 19:
      return especiais[num - 10]
  elif 20 <= num <= 99:
      dezena = num // 10
      unidade = num % 10
      if unidade == 0:
          return dezenas[dezena]
      else:
          return f"{dezenas[dezena]} e {unidades[unidade]}"
  else:
      return "Número fora do intervalo permitido."

def main():
  while True:
      try:
          num = int(input("Digite um número entre 0 e 99: "))
          if 0 <= num <= 99:
              print(f"O número {num} por extenso é: {numero_por_extenso(num)}")
              break
          else:
              print("Número fora do intervalo permitido. Tente novamente.")
      except ValueError:
          print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
  main()
