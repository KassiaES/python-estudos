'''
Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
'''

from colorama import init, Fore, Style
init()

salario = float(input('Digite o salário: '))

if salario <= 1903.98:
    aliquota = 0
elif salario <= 2826.65:
    aliquota = 0.075
elif salario <= 3751.05:
    aliquota = 0.15
elif salario <= 4664.68:
    aliquota = 0.225
else:
    aliquota = 0.275

imposto_de_renda = salario * aliquota
salario_liquido = salario - imposto_de_renda

print(f"Salário Bruto: {Fore.GREEN}R$ {salario:.2f}{Style.RESET_ALL}")
print(f"Alíquota do Imposto de Renda: {Fore.RED}{aliquota * 100:.1f}%{Style.RESET_ALL}")
print(f"Valor do Imposto de Renda: {Fore.RED}R$ {imposto_de_renda:.2f}{Style.RESET_ALL}")
print(f"Salário Líquido: {Fore.GREEN}R$ {salario_liquido:.2f}{Style.RESET_ALL}")