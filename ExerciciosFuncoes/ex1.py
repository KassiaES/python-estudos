'''
Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos
'''

def soma(numero1, numero2, numero3):
    soma = numero1 + numero2 + numero3
    print(f'A soma dos números é: {soma}')

print('Digite 3 números inteiros para a soma')
numeros = []
for i in range(3): 
    numero = int(input(f'Digite o número {i + 1}: '))
    numeros.append(numero)

soma(numeros[0], numeros[1], numeros[2])