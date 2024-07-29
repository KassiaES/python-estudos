'''
Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais.
'''

def contar_vogais(string):
    vogais = "AEIOU"
    count = 0
    for char in string:
        if char in vogais:
            count += 1
    return count

frase = input("Digite uma frase: ").upper()
total_vogais = contar_vogais(frase)
print(f"A frase contém {total_vogais} vogais.")