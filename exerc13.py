def metros_para_centimetros(metros):
    centimetros = metros * 100
    return centimetros

#exemplo de uso
metros = float(input("digite o valor em metros: "))
centimetros = metros_para_centimetros(metros)
print(f"{metros} metros e igual a {centimetros} centimetros.")
