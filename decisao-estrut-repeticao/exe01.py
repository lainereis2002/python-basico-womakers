'''faça um programa que peça dois numero e imprima o maior deles'''

numero01 = int(input("Digite o primeiro numero: "))
numero02 = int(input("Digite o segundo numero: "))

if numero01 > numero02:
    print(f"o maior numero é o primeiro: {numero01}")
else:
    print(f"o maior numero é o segundo: {numero02}")