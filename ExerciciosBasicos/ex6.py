'''
Escreva um programa que calcule o tempo de uma viagem. 
Faça um comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h
'''

distancia = float(input('Digite a distância em quilômetros: '))

tempo_aviao = distancia / 600
tempo_carro = distancia / 100
tempo_onibus = distancia / 80

print(f"Para uma viagem de {distancia}km equivalem a:")
print(f"Tempo de viagem de avião: {tempo_aviao:.2f} horas")
print(f"Tempo de viagem de carro: {tempo_carro:.2f} horas")
print(f"Tempo de viagem de ônibus: {tempo_onibus:.2f} horas")