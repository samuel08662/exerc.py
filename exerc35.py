# Pergunta ao usuário o tamanho da área em metros quadrados
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Cálculo da quantidade de tinta necessária
litros_necessarios = area / 3  # 1 litro cobre 3 m²
latas_necessarias = litros_necessarios / 18  # Cada lata tem 18 litros

# Arredonda para cima, pois não podemos comprar uma fração de lata
import math
latas_necessarias = math.ceil(latas_necessarias)

# Cálculo do preço total
preco_por_lata = 80.00
preco_total = latas_necessarias * preco_por_lata

# Exibe os resultados
print(f"Quantidade de latas de tinta a serem compradas: {latas_necessarias}")
print(f"Preço total: R${preco_total:.2f}")
