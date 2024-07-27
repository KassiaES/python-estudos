'''
Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).
'''
from colorama import init, Fore, Style
init()

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))

imc = peso/(altura * altura)

print(f"O Índice de Massa Corporal é: {Fore.BLUE}{imc:.2f}{Style.RESET_ALL}")