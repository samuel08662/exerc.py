def verificar_bissexto(ano):
    """
    Verifica se um ano é bissexto.
    :param ano: O ano a ser verificado
    :return: True se o ano for bissexto, False caso contrário
    """
    if (ano % 4 == 0):
        if (ano % 100 == 0):
            if (ano % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    ano = int(input("Digite um ano para verificar se é bissexto: "))
    if verificar_bissexto(ano):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

if __name__ == "__main__":
    main()
