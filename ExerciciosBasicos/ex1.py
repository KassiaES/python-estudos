'''
Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão
'''

from colorama import init, Fore, Style
init()

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print('Soma = {} \nSubtração = {} \nMultiplicação = {} \nDivisão {:.2f}' .format(soma,subtracao,multiplicacao,divisao))

print(f'{Fore.GREEN}Soma = {soma}{Style.RESET_ALL} {Fore.RED}\nSubtração = {subtracao}{Style.RESET_ALL} {Fore.YELLOW}\nMultiplicação = {multiplicacao}{Style.RESET_ALL} {Fore.BLUE}\nDivisão = {divisao:.2f}{Style.RESET_ALL}')