'''crie um dicionario representando um carrinho de compras
adicione produtos (chaves) e quantidades ao carrinho
calcule o total do carrinho de compra'''

carrinho = {}
carrinho['Banana'] = 2
carrinho['Macarrao'] = 3
carrinho['Feijão'] = 5
carrinho['Carne'] = 3
carrinho['Cebola'] = 6

preco = {
    'Banana': 2.72,
    'Macarrao': 6.69,
    'Feijão': 9.50,
    'Carne': 23.19,
    'Cebola': 0.68
}

total = 0.0
for produto, quantidade in carrinho.items():
    if produto in preco:
        total += preco[produto] * quantidade

print("Carrinho de Compras:")
for produto, quantidade in carrinho.items():
    print(f"{produto}: {quantidade} unidades")

print(f"\nTotal do Carrinho: R${total:.2f}")