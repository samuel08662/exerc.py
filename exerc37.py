import math

# Pergunta ao usuário o valor de A
a = float(input("Digite o valor de A: "))

# Verifica se A é igual a zero
if a == 0:
    print("A equação não é do segundo grau (A não pode ser zero).")
else:
    # Pergunta os valores de B e C
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    # Calcula o delta
    delta = (b ** 2) - (4 * a * c)

    # Verifica as condições do delta
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"A equação possui apenas uma raiz real: {raiz:.2f}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}")
