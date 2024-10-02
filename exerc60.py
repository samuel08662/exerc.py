# Solicita ao usuário o número da tabuada
numero = int(input("Montar a tabuada de: "))

# Solicita ao usuário o valor inicial e final da tabuada
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

print(f"Tabuada de {numero} começando em {inicio} e terminando em {fim}: ")

# Laço para calcular e exibir a tabuada no intervalo especificado
for i in range(inicio, fim + 1):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")
