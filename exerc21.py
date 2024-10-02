import math


def bhaskara(a, b, c):
    # Verifica se a é zero
    if a == 0:
        raise ValueError("O coeficiente 'a' deve ser diferente de zero por ser uma     equação do 2º grau.")

    # Calcula o discriminante
    delta = b**2 - 4*a*c

    if delta < 0:
        return "A equação não possui raízes reais."

    elif delta == 0:
        # Uma raiz real
        x = -b / (2 * a)
        return f"A equação tem uma raiz real: x = {x:.2f}"

    else:
        # Duas raízes reais
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"A equação tem duas raízes reais: x1 = {x1:.2f} e x2 = {x2:.2f}"

def classificar_equacao(a, b, c):
    if b != 0 and c != 0:
        return "Equação completa"
    else:
        return "Equação incompleta"

def main():
    # Entrada dos coeficientes
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))

    tipo_equacao = classificar_equacao(a, b, c)
    print(f"Classificação da equação: {tipo_equacao}")

    if tipo_equacao == "Equação completa":
        resultado = bhaskara(a, b, c)
        print(resultado)
    else:
        print("Não é possível resolver a equação incompleta com a fórmula de Bhaskara.")

if __name__ == "__main__":
    main()
