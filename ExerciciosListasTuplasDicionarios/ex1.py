'''
Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente""
'''

print('Responda as seguintes perguntas com S para sim e N para não:')
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
numero_sim = 0

for pergunta in perguntas:
    resposta = input(f'{pergunta}').lower()
    if resposta == 's':
        numero_sim += 1

if numero_sim == 5:
    print('Assassino')
elif 3 <= numero_sim <= 4:
    print('Cúmplice')
elif numero_sim == 2:
    print('Suspeita')
else:
    print('Inocente')