'''reverso do numero
faça uma função que retorne o reverso de um numero inteiro informado
por exemplo: 127 -> 721 '''

def reverso(num):
    inverso = str(num)[::-1]
    print(f"O inverso de {num} é {inverso}")

num = int(input("Digite um número inteiro: "))
reverso(num)