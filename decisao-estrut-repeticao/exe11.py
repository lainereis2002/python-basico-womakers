'''escreva um programa que calcule o salário líquido
lembrando de declarar o salario bruto e o percentual de desconto
do imposto de renda
renda até 1903,98 -> isento de imposto de renda
1903,99 até 2826,65 -> aliquota de 7,5%
2826,66 até 3751,05 -> aliquota de 15%
3751,06 até 4664,68 -> aliquota de 22,5%
acima de 4664,68 -> aliquota maxima de 27,5%'''

salario = float(input("Digite o seu salário R$ "))

if salario <= 1903.98:
    print(f"seu salário é isento de impostos")
elif 1903.99 <= salario <= 2826.65:
    desconto = salario * 0.075
    print(f"Seu salário sobre um desconto de 7.5%, logo fica R$ {salario-desconto}")
elif 2826.66 <= salario <= 3751.05:
    desconto = salario * 0.15
    print(f"Seu salário sobre um desconto de 15%, logo fica R$ {salario-desconto}")
elif 3751.06 <= salario <= 4664.68 :
    desconto = salario * 0.225
    print(f"Seu salário sobre um desconto de 22.5%, logo fica R$ {salario-desconto}")
else:
    desconto = salario * 0.275
    print(f"Seu salário sobre um desconto de 27.5%, logo fica R$ {salario-desconto}")