def contar_divisoes(n):
  divisões = 0
  primos = []

  def é_primo(num):
      if num <= 1:
          return False
      if num == 2:
          return True
      if num % 2 == 0:
          return False
      for i in range(3, int(num**0.5) + 1, 2):
          nonlocal divisões
          divisões += 1
          if num % i == 0:
              return False
      return True

  for i in range(2, n + 1):
      if é_primo(i):
          primos.append(i)

  return primos, divisões

def main():
  N = int(input("Digite um número inteiro N: "))
  primos, divisões = contar_divisoes(N)
  print(f"Números primos entre 1 e {N}: {primos}")
  print(f"Número de divisões realizadas: {divisões}")

if __name__ == "__main__":
  main()