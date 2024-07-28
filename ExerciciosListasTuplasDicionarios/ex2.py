'''
Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0.
'''
medias = []
contador = 0

for i in range(5):
    print(f'Aluno {i + 1}:')
    notas_aluno = []

    for j in range(4):
        nota = float(input(f'Digite a nota {j + 1}: '))
        notas_aluno.append(nota)
    
    media = sum(notas_aluno) / len(notas_aluno)
    medias.append(media) 

contador = sum(1 for media in medias if media >= 7.0)

print(f'Número de alunos com média maior ou igual a 7.0: {contador}')