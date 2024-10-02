import math

# solicita um numero inteiro ao usuario
numero = int(input("digite um numero inteiro: "))
# verifique se o numero e menor ou igual a 1
if numero <= 1:
  print(f"{numero} nao e um numero primo. ")
else:
     #assume que o numero e primo
     primo = True 
     # verifique se o numero e divisel por algum numero de 2 ate a raiz quadrada de numero
     for i in range(2, int(math.sqrt(numero))+ 1):
        if numero % i == 0:
          primo = False
          break

     #exiba se o numero e primo ou nao 
     if primo:
         print(f" {numero} e um numero primo.  ")
     else:
         print(f" {numero} nao e um numero primo. ")
       