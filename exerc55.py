import re 

# solicita ao usuario que informe uma sequencia de caracteres
sequencia = input("digite uma sequencia de caracteres: ")

#remova todos os espacos e pontuacoes e transforma em minusculas
sequencia_normalizada = re.sub(r'[^a-zA-Z0-9]',  ' ', sequencia).lower()

# verifique se a sequencia e um palindromo 
if sequencia_normalizada == sequencia_normalizada[ - 1: -1: -1]:
  print("a sequencia e um palindromo. ")
else:
  print(" a sequencia nao e um palindromo.  ")