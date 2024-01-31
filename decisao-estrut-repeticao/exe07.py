'''desenvolver um programa que solicite a idade do usuário e identifique
se ele é uma criança, um adolescente, adulto ou idoso'''

idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Usuário é uma criança")
elif 12 <= idade < 18:
    print("usuário é um adolescente")
elif 18 <= idade < 65:
    print("Uusário é um adulto")
else:
    print("Usuário é um idoso")