'''
Faça um programa que lê três números inteiros e os mostra em ordem
crescente.
'''

numero1 = int(input('Digite o primeiro número inteiro: '))
numero2 = int(input('Digite o segundo número inteiro: '))
numero3 = int(input('Digite o terceiro número inteiro: '))

if numero1 <= numero2 and numero1 <= numero3:
    if numero2 <= numero3:
        menor, meio, maior = numero1, numero2, numero3
    else:
        menor, meio, maior = numero1, numero3, numero2
elif numero2 <= numero1 and numero2 <= numero3:
    if numero1 <= numero3:
        menor, meio, maior = numero2, numero1, numero3
    else:
        menor, meio, maior = numero2, numero3, numero1
else:
    if numero1 <= numero2:
        menor, meio, maior = numero3, numero1, numero2
    else:
        menor, meio, maior = numero3, numero2, numero1

print(f'Os números em ordem crescente são: {menor}, {meio}, {maior}')