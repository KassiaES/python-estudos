'''
Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.
'''

carrinho_compras = {}

carrinho_compras['pão'] = 5.60
carrinho_compras['leite'] = 7.00
carrinho_compras['ovos'] = 15.50
carrinho_compras['farinha'] = 14.20

total = 0
for produto, valor in carrinho_compras.items():
    total += valor

print("\nLista de produtos no carrinho:")
for produto, valor in carrinho_compras.items():
    print(f'{produto}: R$ {valor:.2f}')
print(f'Total do carrinho de compras: R$ {total:.2f}')
