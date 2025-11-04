
with open("dados_alunos.txt", "r") as file:
    linha = file.read()
    
    nova_linha = (linha.split("#"))

    print(nova_linha[0])


