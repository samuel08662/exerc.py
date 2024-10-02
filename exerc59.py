# Dados iniciais
populacao_A = 80000
populacao_B = 200000
taxa_crescimento_A = 0.03
taxa_crescimento_B = 0.015
anos = 0

# Loop para calcular o número de anos
while populacao_A < populacao_B:
    populacao_A *= (1 + taxa_crescimento_A)
    populacao_B *= (1 + taxa_crescimento_B)
    anos += 1

print(f"Número de anos necessários: {anos}")
