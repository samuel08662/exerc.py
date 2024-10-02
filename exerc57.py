# inicializa o contador de resposta afirmativas
contador_resposta_afirmativa = 0 

#lista de perguntas e respostas corretas 
perguntas = [
  "telefonou para a vitima?, 1 - sim, 0 - nao ",
  "esteve no local do crime?, 1 - sim, 0 - nao  ",
  " mora perto da vitima?, 1 - sim, 0 - nao  ",
  "devia para a vitima?, 1 - sim, 0 - nao  ",
  "trabalhou com a vitima?, 1 - sim, 0 - nao  ",
]

# faz as perguntas e contas as respostas afirmativas
for pergunta in perguntas:
  resposta = input(pergunta).strip().lower()
  if resposta == '1' or resposta == 'sim':
    contador_resposta_afirmativa += 1 

# classifica a pessoa com base no numero de respostas afirmativas 
if contador_resposta_afirmativa == 2:
  print("suspeito ")
elif 3 <= contador_resposta_afirmativa <= 4:
  print("cumplice")
elif contador_resposta_afirmativa == 5:
  print("assasino")
else: 
  print("inocente")

print(f"a pessoa e classificada como: {contador_resposta_afirmativa}  ")

  
