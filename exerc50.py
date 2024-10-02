# solicita ao usuario o numero inteiro desejado 
numero = int(input("digite um numero inteiro para calcular fatorial: " ))
# inicializa a variavel fatorial com 1 
fatorial = 1
# verifica se o numero e negativo, zero ou positivo
if numero < 0:
  print(" o fatorial nao e definido para numeros negativos:   ")
else:
  # calcula o fatorial do numero usando um loop for
  for _i in range(1, numero + 1):
    fatorial *= _i
# exiba o resultado do fatorial    
print(f" o fatorial de {numero} e {fatorial}  ")
