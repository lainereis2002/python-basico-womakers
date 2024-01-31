'''criar um programa que solicite 3 numeros ao usuario
utilize estruturas condicionais para determinar o maior
entre eles e apresente o resultado'''

num01 = int(input("Digite o primeiro número: "))
num02 = int(input("Digite o segundo número: "))
num03 = int(input("Digite o terceiro número: "))

if num01 > num02 and num01 > num03:
    print(f"o maior numero é o primeiro: {num01}")
elif num02 > num01 and num02 > num03:
    print(f"o maior numero é o segundo: {num02}")
else:
    print(f"o maior numero é o terceiro: {num03}")