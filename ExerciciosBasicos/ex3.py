'''
Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.
'''

quilometros = float(input('Digite a quantidade de quilômetros: '))
metros = quilometros * 1000
centimetros = metros * 100
milimetros = centimetros * 10

print(f"{quilometros} quilômetros equivalem a:")
print(f"{metros:.0f} metros")
print(f"{centimetros:.0f} centímetros")
print(f"{milimetros:.0f} milímetros")