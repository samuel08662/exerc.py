# pre-calcula todos os numeros de fibonacci ate o 59° termo  
def calcular_fibonacci():
    fib = [0] * 60  # vetor com 60 posicoes (de 0 a 59)
    fib [0] = 0 
    fib [1] = 1  
    for _i in range(2, 60):
     fib[_i] = fib[_i-1] + fib[_i-2]
    return fib 

# leitura do numero de casos de teste
T = int(input("digite o numero de casos de teste: "))

# calcula toda a sequencia de fibonacci ate o 59° termo 
fib = calcular_fibonacci()

# loop para cada caso de teste 
for _ in range(T):
    n = int(input()) # leitura do valor de n
print(f"fib ({n}) = {fib[n]}")