from random import randint

def classifica_times(times):
    # Ordenar por pontos, vitórias, saldo de gols, gols pró, e sorteio em caso de empate.
    times.sort(key=lambda time: (-time['pontos'], -time['vitorias'], -time['saldo_gols'], -time['gols_pro']), reverse=True)

    # Caso de empate, realizar um sorteio
    for i in range(1, len(times)):
        if times[i]['pontos'] == times[i-1]['pontos'] and times[i]['vitorias'] == times[i-1]['vitorias'] and times[i]['saldo_gols'] == times[i-1]['saldo_gols'] and times[i]['gols_pro'] == times[i-1]['gols_pro']:
            sorteio = randint(0, 1)  # Sorteio aleatório entre 0 e 1
            if sorteio == 0:
                times[i], times[i-1] = times[i-1], times[i]  # Troca a posição dos times em caso de empate

    return times