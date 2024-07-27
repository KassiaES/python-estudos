'''
Faça um Programa que peça dois números e imprima o maior deles.
'''

numero1 = float(input('Digite primeiro número: '))
numero2 = float(input('Digite segundo número: '))

if (numero1 > numero2):
    print(f'O número maior é: {numero1}')
elif (numero2 > numero1):
    print(f'O número maior é: {numero2}')
else:
    print(f"Os números são iguais")