def jogar_jogo_da_velha():
    """
    Função para jogar o Jogo da Velha.
    """
    # Cria o tabuleiro
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

    # Define os jogadores
    jogador_atual = 'X'

    # Loop principal do jogo
    while True:
        # Imprime o tabuleiro
        print_tabuleiro(tabuleiro)

        # Pede ao jogador atual para fazer a jogada
        linha, coluna = obter_jogada(jogador_atual)

        # Faz a jogada
        tabuleiro[linha][coluna] = jogador_atual

        # Verifica se o jogador atual ganhou
        if verificar_vitoria(tabuleiro, jogador_atual):
            # Imprime o tabuleiro
            print_tabuleiro(tabuleiro)
            print(f'O jogador {jogador_atual} ganhou!')
            break

        # Verifica se o jogo empatou
        if verificar_empate(tabuleiro):
            # Imprime o tabuleiro
            print_tabuleiro(tabuleiro)
            print('O jogo empatou!')
            break

        # Muda o jogador atual
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

def print_tabuleiro(tabuleiro):
    """
    Imprime o tabuleiro do Jogo da Velha.
    """
    print('---------')
    for linha in tabuleiro:
        print('|', end='')
        for coluna in linha:
            print(f' {coluna} |', end='')
        print('\n---------')

def obter_jogada(jogador):
    """
    Pede ao jogador atual para fazer a jogada.
    """
    while True:
        try:
            linha = int(input(f'Jogador {jogador}, insira a linha (0-2): '))
            coluna = int(input(f'Jogador {jogador}, insira a coluna (0-2): '))
            if 0 <= linha <= 2 and 0 <= coluna <= 2 and tabuleiro[linha][coluna] == ' ':
                return linha, coluna
            else:
                print('Jogada inválida. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Tente novamente.')

def verificar_vitoria(tabuleiro, jogador):
    """
    Verifica se o jogador atual ganhou.
    """
    # Verifica linhas
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True

    # Verifica colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == jogador and tabuleiro[1][coluna] == jogador and tabuleiro[2][coluna] == jogador:
            return True

    # Verifica diagonais
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    # Nenhuma vitória
    return False

def verificar_empate(tabuleiro):
    """
    Verifica se o jogo empatou.
    """
    for linha in tabuleiro:
        for coluna in linha:
            if coluna == ' ':
                return False

    # Tabuleiro cheio, jogo empatou
    return True

# Iniciar o jogo
jogar_jogo_da_velha()