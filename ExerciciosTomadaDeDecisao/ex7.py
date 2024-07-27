'''
Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.
'''

idade = int(input('Digite a sua idade: '))

if (idade > 0 and idade <= 12):
    print('Você é uma criança')
elif (idade > 12 and idade < 18):
    print('Você é um(a) adolescente')
elif (idade > 17 and idade < 60):
    print('Você é um(a) adulto(a)')
elif (idade > 59 and idade <= 105):
    print('Você é um(a) idoso(a)')
else:
    print('Valor inválido')