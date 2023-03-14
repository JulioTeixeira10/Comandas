with open("comanda.txt", "w") as f:
    for i in range(1, 151):
        comanda = f"COMANDA: {i:03}\n"
        nome = "NOME:________________________________________________TEL: _______________\n"
        acompanhante = "ACOMPANHANTE:___________________ _________________________ _________________\n\n"
        f.write(comanda + nome + acompanhante)