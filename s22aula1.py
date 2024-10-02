# entrada dos dados dos funcionarios 
numero_funcionarios = int(input("digite o numero do funcionario: "))
horas_trabalhadas = float(input("digite o numero de horas trabalhadas: "))
valor_por_hora = float(input("digite o valor que o funcionario recebe por horas: "))
# calcula o salario do funcionario 
salario = horas_trabalhadas * valor_por_hora
# saida com o formato solicitado 
print(f"NUMBER = {numero_funcionarios}")
print(f"SALARY = U$ {salario: .2f} ")


