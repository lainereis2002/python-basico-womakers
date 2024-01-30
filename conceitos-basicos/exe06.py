'''solicite ao usuário o peso em kg e a altura em metros
calcule e imprima o IMC usando a formula
IMC = peso / (altura*altura)'''

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura*altura)
print(f"seu IMC é de {imc:.2f}")