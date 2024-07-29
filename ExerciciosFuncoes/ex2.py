'''
Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.
'''

def inverter_numero(numero):
    return int(str(numero)[::-1])

try:
    numero = int(input("Digite um número inteiro positivo: "))
    numero_invertido = inverter_numero(numero)
    print("Número invertido:", numero_invertido)
except ValueError:
    print("Erro: Por favor, insira um número inteiro válido.")