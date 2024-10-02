# solicita ao usuario o total de eleitores
total_eleitores = int(input("digite o total de eleitores: "))
# inicializa a contagem de votos para cada candidato
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
# loop para que cada eleitor vote
for _i in range(total_eleitores):
   print("n\ eleitor" , _i + 1 )
   print(" vote 1 para candidato: 1 ")
   print(" vote 2 para candidato: 2 ")
   print(" vote 3 para candidato: 3 ")
   voto = int(input("digite o numero do seu candidato:  "))
  # registra o voto para o candidato escolhido 
   if voto == 1:
     votos_candidato1 += 1 
   elif voto == 2:
     votos_candidato2 += 1 
   elif voto == 3:
     votos_candidato3 += 1 
   else:
     print("voto invalido. tente novamente. ")

   # exiba o numero de votos de cada candidato
   print("\n resultado da eleicao:  ")
   print(f" candidato 1: {votos_candidato1} votos ")
   print(f" candidato 2: {votos_candidato2} votos ")
   print(f" candidato 3: {votos_candidato3} votos ")