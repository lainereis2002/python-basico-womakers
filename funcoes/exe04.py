'''crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e calcule quanto poderia comprar de cada moeda estrangeira
considere a tabela de conversão abaixo:
dolar americano: 4,91
peso argentino: 0,02
dolar australiano: 3,18
dolar canadense: 3,64
franco suiço: 0,42
euro: 5,36
libra esterlina: 6,21'''

carteira = float(input("Digite quanto você possui em sua carteira: R$ "))
print(f"Você conseguiria comprar ${carteira*4.91:.2f} em Dólar Americano")
print(f"Você conseguiria comprar ${carteira*0.02:.2f} em Peso Argentino")
print(f"Você conseguiria comprar ${carteira*3.18:.2f} em Dólar Australiano")
print(f"Você conseguiria comprar ${carteira*3.64:.2f} em Dólar Canadense")
print(f"Você conseguiria comprar ${carteira*0.42:.2f} em Franco Suiço")
print(f"Você conseguiria comprar ${carteira*5.36:.2f} em Euro")
print(f"Você conseguiria comprar ${carteira*6.21:.2f} em Libra Esterlina")