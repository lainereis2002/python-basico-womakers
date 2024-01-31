'''faça um programa que peça uma nota, entre zero e dez
mostre uma mensagem caso o valor seja inválido
e continue pedindo até que o usuário informe um valor válido'''

numero = int(input("Digite um valor de 0 a 10: "))
while True:
    if 0 <= numero <= 10:
        print("Numero válido")
        break
    else:
        print("numero inválido")
        numero = int(input("Digite um valor de 0 a 10: "))
        
