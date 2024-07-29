'''
Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.
'''

numero = int(input("Digite um número inteiro: "))

numero_invertido = int(str(numero)[::-1])

print("Número invertido:", numero_invertido)