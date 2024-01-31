'''desenvolva um programa que solicite ao suario os comprimentos
dos 3 lados de um triangulo e classifique-o como:
equilátero - todos os lados com o mesmo valor
isosceles - dois lados com o mesmo valor
escaleno - todos os lados com medidas distintas'''

lado1 = float(input("Digite o valor do lado 1: "))
lado2 = float(input("Digite o valor do lado 2: "))
lado3 = float(input("Digite o valor do lado 3: "))

if lado1 == lado2 == lado3:
    print("Triângulo equilátero")
elif lado1 != lado2 != lado3:
    print("Triângulo escaleno")
else:
    print("Triângulo isósceles")