# precos dos combutiveis
preco_alcool = 3.90
preco_gasolina = 5.30


# descontos
desconto_alcool_ate_20 = 0.03
desconto_alcool_acima_de_20 = 0.05
desconto_gasolina_ate_20 = 0.04
desconto_gasolina_acima_de_20 = 0.06
preco_por_litro = 0 
desconto = 0

# leitura de dados 
litros = float(input("digite o numero de litros vendidos: "))
tipo_combustivel = input("digite o tipo de combustivel (a-alcool, g-gasolina):  ")

# calculo do valor a ser pago 
if tipo_combustivel == 'a':
  preco_por_litro = preco_alcool
  if litros <= 20:
    desconto = desconto_alcool_ate_20
  else:
     desconto = desconto_alcool_acima_de_20
elif tipo_combustivel == 'g':
  preco_por_litro = preco_gasolina
  if litros <= 20:
     desconto  =  desconto_gasolina_ate_20
  else: 
    desconto = desconto_gasolina_acima_de_20
else:
  print(" o tipo de combustivel digitado nao e valido.")
  

# calcula o valor total sem desconto 
valor_total = litros * preco_por_litro

# calcula o valor com desconto 
valor_com_desconto = valor_total * desconto 

# clcula o valor  final a ser pago 
valor_final = valor_total - valor_com_desconto

# exiba o valor final a ser pago 
print(f"o valor a ser pago e: rs {valor_final}")
    

    
    

