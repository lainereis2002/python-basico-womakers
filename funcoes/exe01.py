'''faça um programa com uma função que necessite de 3 argumentos
e que forneça a soma desses tres argumentos'''
def soma(num1, num2, num3):
    calculo = num1 + num2 + num3
    print(f"A soma de {num1} + {num2} + {num3} = {calculo}")

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
soma(num1, num2, num3)