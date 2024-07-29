'''
Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21
'''

def calcular_conversao(reais, taxa_cambio):
    return reais / taxa_cambio

def exibir_conversao(reais):
    dolar_americano = 4.91
    peso_argentino = 0.02
    dolar_australiano = 3.18
    dolar_canadense = 3.64
    franco_suico = 0.42
    euro = 5.36
    libra_esterlina = 6.21

    print(f"Com R${reais:.2f} você pode comprar:")
    print(f"{calcular_conversao(reais, dolar_americano):.2f} Dólares Americanos")
    print(f"{calcular_conversao(reais, peso_argentino):.2f} Pesos Argentinos")
    print(f"{calcular_conversao(reais, dolar_australiano):.2f} Dólares Australianos")
    print(f"{calcular_conversao(reais, dolar_canadense):.2f} Dólares Canadenses")
    print(f"{calcular_conversao(reais, franco_suico):.2f} Francos Suiços")
    print(f"{calcular_conversao(reais, euro):.2f} Euros")
    print(f"{calcular_conversao(reais, libra_esterlina):.2f} Libras Esterlinas")

try:
    reais = float(input("Digite quanto dinheiro você tem na carteira em reais: "))
    if reais < 0:
        raise ValueError("O valor não pode ser negativo.")
    exibir_conversao(reais)
except ValueError as e:
    print(f"Erro: {e}. Por favor, insira um valor numérico válido.")

