'''
Crie duas tuplas. Concatene-as para formar uma nova tupla.
'''

elementos1 = []
print('Digite 3 números inteiros para a primeira tupla:')
for i in range(3):
    numero = int(input(f'Digite o elemento {i + 1}: '))
    elementos1.append(numero)

tupla1 = tuple(elementos1)

elementos2 = []
print('Digite 3 números inteiros para a segunda tupla:')
for i in range(3): 
    numero = int(input(f'Digite o elemento {i + 1}: '))
    elementos2.append(numero)

tupla2 = tuple(elementos2)

tupla_concatenada = tupla1 + tupla2

print("Primeira tupla:", tupla1)
print("Segunda tupla:", tupla2)

print("Tupla concatenada:", tupla_concatenada)
