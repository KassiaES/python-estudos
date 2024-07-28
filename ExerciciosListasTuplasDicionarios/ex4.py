'''
Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.
'''

contatos = {
    'João': '1234-5678',
    'Maria': '9876-5432',
    'Ana': '5555-1234',
    'Carlos': '4321-8765'
}

nome_procurado = input("\nDigite o nome do contato que deseja procurar: ")

if nome_procurado in contatos:
    print(f'Telefone de {nome_procurado}: {contatos[nome_procurado]}')
else:
    print(f'Contato "{nome_procurado}" não encontrado.')