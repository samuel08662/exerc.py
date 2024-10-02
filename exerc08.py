#recebe uma letra do usuario
letra = input("digite uma letra: ").lower()

#verefica se a entrada e uma unica letra
if len(letra) != 1 or not letra.isalpha():
    print("entrada invalida. por favor, digite uma unica letra.")
else:
#conjuto de vogais
 vogais = "aeiou"

#verefica se a letra e vogal ou consoante 
if letra in vogais:
   print("a letra e uma vogal.")
else:
   print("a letra e uma consoante.")