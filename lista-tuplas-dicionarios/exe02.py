'''faça um programa que peça as quatro notas de 5 alunos
calcule e armazene numa lista a média de cada aluno
imprima o número de alunos com a média maior ou iguala 7.0'''

medias = []
cont = 0

for aluno in range(5):
    nota1 = float(input("\nDigite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    media = (nota1+nota2+nota3+nota4)/4
    medias.append(media)

print(f"\n{medias}")

for num in medias:
    if num <= 7.0:
        cont += 1

print(f"\n{cont} alunos tiveram média igual ou maior que 7.0")
