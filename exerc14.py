#solicite ao usuario para solicitar uma letra
letra = input("digite 'F' para feminino ou 'M' para masculino: ").strip().upper()

#verefique e imprime a mensagem correspondente
if letra == 'F':
    print("F - feminino")
elif letra == 'M':
    print("M- masculino")
else:
    print("sexo invalido")
