'''
Peça ao usuário para informar o ano de nascimento.
Em seguida,calcule e imprima a idade atual
'''

from datetime import datetime

ano_de_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = datetime.now().year

print(f'A idade atual é {ano_atual-ano_de_nascimento}')