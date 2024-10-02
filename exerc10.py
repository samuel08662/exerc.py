# funcao para determinar o tipo do triangulo
def tipo_triangulo(lado1, lado2, lado3):
  #verifique se os lados formam um triangulo
  if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3
                                                              > lado1):
    # verifique o tipo de triangulo
    if lado1 == lado2 == lado3:
      return "equilatero"
    elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
      return "isosceles"
    else:
      return "escaleno"
  else:
    return "os lados fornecidos nao formam um triangulo "


# funcao principal
def main():
  # entrada  dos lados do triangulo
  lado1 = float(input("digite o valor do primeiro lado:  "))
  lado2 = float(input("digite o valor do segundo lado: "))
  lado3 = float(input("digite o valor do terceiro lado:  "))
  # exiba o tipo de triangulo
  print(tipo_triangulo(lado1, lado2, lado3))


if __name__ == "__main__":
  main()
