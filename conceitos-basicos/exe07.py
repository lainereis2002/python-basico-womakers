'''faça um programa que pergunte quanto voce ganha por hora
e o numero de horas trabalhadas no mês.
calcule e mostre o total do seu salário no referido mês'''

dinheiro = float(input("digite o quanto voce ganha por hora trabalhada: "))
horas = int(input("digite quantas horas voce trabalha no mês: "))
print(f"SEU SALÁRIO MENSAL É DE R$ {((dinheiro*horas)*30):.2f}")