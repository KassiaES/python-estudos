'''
Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.
'''

horas_semana = float(input('Digite o número de horas de exercícios físicos por semana: '))
minutos_semana = horas_semana * 60
minutos_mes = minutos_semana * 4

calorias = minutos_mes * 5

print(f'O total de calorias queimadas em um mês é: {calorias:.0f}')