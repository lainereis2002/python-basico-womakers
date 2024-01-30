'''solicite ao usuário o numero de horas de exercicio físico por semana
calcule o total de calorias queimadas em um mes
considerando uma média de 5 kcal por minuto de exercicio'''

horas = int(input("digite a quantidade de horas que voce realiza exercicio físico por semana: "))
kcalPorHora = 5*(horas*60)
print(f"A quantidade de kcal queimadas em um mês é de {kcalPorHora*4}")