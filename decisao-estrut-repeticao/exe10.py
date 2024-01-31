'''faça um programa que lê 3 numeros inteiros
e os mostra em ordem crescente'''
num01 = int(input("Digite o primeiro numero: "))
num02 = int(input("Digite o segundo numero: "))
num03 = int(input("Digite o terceiro numero: "))

if num01 > num02 and num01 > num03:
    if num02 > num03:
        print(f"o os numeros em ordem crescente: {num01} - {num02} - {num03}")
    else:
        print(f"o os numeros em ordem crescente: {num01} - {num03} - {num02}")
elif num02 > num01 and num02 > num03:
    if num01 > num03:
        print(f"o os numeros em ordem crescente: {num02} - {num01} - {num03}")
    else:
        print(f"o os numeros em ordem crescente: {num02} - {num03} - {num01}")
else:
    if num01 > num02:
        print(f"o os numeros em ordem crescente: {num03} - {num01} - {num02}")
    else:
        print(f"o os numeros em ordem crescente: {num03} - {num02} - {num01}")