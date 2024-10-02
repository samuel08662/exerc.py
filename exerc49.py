def fibonacci(n):
    # Verifica se o número de termos é menor ou igual a 0
    if n <= 0:
        return []
    elif n == 1:
        return [1]

    # Inicializa a lista com os primeiros dois termos da série
    fib_series = [1, 1]

    # Calcula os termos subsequentes até o n-ésimo termo
    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series

# Solicita ao usuário o número de termos desejados
n = int(input("Digite o número de termos desejados para a série de Fibonacci: "))

# Gera e exibe a série
fib_series = fibonacci(n)
print(f"Série de Fibonacci até o {n}-ésimo termo: {fib_series}")
