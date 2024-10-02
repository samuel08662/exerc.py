#recebe o nome da disciplina
disciplina = input("digite o nome da disciplina: ")

#recebe as 4 notas do aluno
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
nota4 = float(input("digite a quarta nota: "))

#calcula a media das notas
media = (nota1 + nota2 + nota3 + nota4) / 4 

#determina a condição do aluno
if media >= 7:
    condicao = "aprovado"
else:
    condicao = "reprovado"

# imprime o resultado
print(f"disciplina: {disciplina}")
print(f"media: {media:.2f}")
print(f"condicao: {condicao}")