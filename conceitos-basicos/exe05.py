'''escreva um programa que calcule o tempo de uma viagem
faça um comparativo do mesmo percurso feito de 
avião = 600km/h
carro = 100km/h
onibus = 80km/h'''
distancia = float(input("Digite a distancia a ser percorrida: "))
aviao = distancia/600
carro = distancia/100
onibus = distancia/80
print(f"O tempo num avião seria {aviao:.2f} horas, num carro seria de {carro:.2f} horas e num onibus seria de {onibus:.2f} horas")