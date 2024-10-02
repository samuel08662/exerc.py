#solicita ao usuario um valor
valor = float(input("digite um valor: "))

#verifica se o valor e possitivo, negativo ou zero
if valor > 0:
    print("o valor e positivo.")
elif valor < 0:
    print("o valor e negativo.")
else:
    print("o valor e zero.")