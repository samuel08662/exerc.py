def inicio():
    turno = input("Em que turno você estuda? (M-matutino, V-vesperino, N-noturno): ").strip().upper()
    
    if turno == "M":
        print("Bom dia!")
    elif turno == "V":
        print("Boa tarde!")
    elif turno == "N":
        print("Boa noite!")
    else:
        print("Valor inválido!")

inicio()
