'''
Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área.
'''
from colorama import init, Fore, Style
init()

nome = input('Digite seu nome: ').upper()
cidade = input('Digite a sua cidade: ')
profissão = input('Digite a sua profissão: ')
idade = int(input('Digite a sua idade: '))

print(f"Olá {Fore.BLUE}{nome}{Style.RESET_ALL}!")
print(f"Felicidade pelos seus {Fore.YELLOW}{idade}{Style.RESET_ALL} anos.")
print(f"Que bom que sua profissão é {Fore.YELLOW}{profissão}{Style.RESET_ALL}.")
print(f"Sua cidade {Fore.YELLOW}{cidade}{Style.RESET_ALL} é ótima!")