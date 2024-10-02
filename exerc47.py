# Solicitar entrada do usuário
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

# Inicializar o resultado
resultado = 1

# calcula a potencia usando um loop
for _ in range(expoente):
      resultado += base 

# Exibir o resultado
print(f"O resultado de {base} elevado a {expoente} é {resultado}")
