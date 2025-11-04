
notas = []
nomes = []

with open("dados_alunos.txt", "r", encoding='utf-8') as arquivo:
    for linha in arquivo:
        nome, curso, nota = linha.strip().split('#')
        nota = float(nota)
        
        nomes.append(nome)
        notas.append(nota)

media = sum(notas) / len(notas)
maior_nota = max(notas)
menor_nota = min(notas)

aluno_maior_nota = nomes[notas.index(maior_nota)]
aluno_menor_nota = nomes[notas.index(menor_nota)]

print(f"Média da turma: {media}")
print(f"Maior nota: {maior_nota} ({aluno_maior_nota})")
print(f"Menor nota: {menor_nota} ({aluno_menor_nota})")
