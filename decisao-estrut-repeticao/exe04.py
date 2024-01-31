'''implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10
se a pontuação for mair ou igual a 7, o aluno é aprovado
caso contrário, é reprovado'''

nota = float(input("Insira uma nota de 0 a 10: "))
if nota >= 7.0:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")