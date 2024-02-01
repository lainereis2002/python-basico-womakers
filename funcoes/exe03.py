'''escreva um script(programa) que pergunta ao usuário se ele deseja converter
uma temperatura de grau celsius para fahrenheit ou vice versa
para cada opção, crie uma função'''

def celsius(valor):
    grauFahrenheit = (valor*(9/5))+32
    print(f"\n{valor}º Celsius é o equivalente a {grauFahrenheit}º Fahrenheit")

def fahrenheit(valor):
    grauCelsius = (valor - 32) * (5/9)
    print(f"\n{valor}º Fahrenheit é o equivalente a {grauCelsius}º Celsius")

grau = float(input("Digite o grau de temperatura: "))
escolha = input("Escolha C ou F para determinar o tipo de temperatura: ").upper()

while escolha != 'C' or escolha != 'F': 
    if escolha == 'C':
        celsius(grau)
        break
    elif escolha == 'F':
        fahrenheit(grau)
        break
    else:
        print("Escolha inválida." )
        escolha = input("Escolha C ou F para determinar o tipo de temperatura: ").upper()
