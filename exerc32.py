# Pergunta ao usuário a temperatura em Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Converte para Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Converte para Kelvin
kelvin = celsius + 273.15

# Exibe os resultados
print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F")
print(f"Temperatura em Kelvin: {kelvin:.2f} K")
