'''
Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função
'''

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu():
    print("Escolha a conversão de temperatura:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    opcao = input("Digite 1 ou 2: ")
    
    if opcao == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
    elif opcao == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit}°F é igual a {celsius:.2f}°C")
    else:
        print("Opção inválida. Por favor, digite 1 ou 2.")
        menu()

menu()