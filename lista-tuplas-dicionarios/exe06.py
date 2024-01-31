'''faça um programa que permita ao usuário digitar o seu nome e em seguida
mostre o nome do usuário de trás para frente utilizando somente letras maiusculas
dica: lembre-se que ao informar o nome o usuário pode digitar letras maísuculas
ou minúsculas'''

nome = input("Digite seu nome: ").upper()
print(nome[::-1])