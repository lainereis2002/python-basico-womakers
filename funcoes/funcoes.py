def soma(num1, num2): #definição da função soma
    calculo = num1 + num2
    print(f"O resultado da soma é: {calculo}")

def subtracao(num1, num2):
    sub = num1 - num2
    print(f"O resultado da subtração é: {sub}")
    multiplicacao(num1, num2) #chamada de funcao dentro de outra funcao

def multiplicacao(num1, num2):
    mult = num1 * num2
    print(f"O resultado da multiplicação é: {mult}")

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

soma(num1, num2) #chamada da função
subtracao(num1, num2)
