# mensagens iniciais para o usuário
print('Olá Mundo!')
print('Olá, esse é meu primeiro código em python!')

#TIPO INTEIRO - int
numero = int(input('Digite seu número:'))
#print("seu numero é:", numero, "\n")
print(f'seu número é {numero} \n')

#TIPO COM VÍRGULA - float
numero2 = float(input('Digite um numero real:'))
#print("seu numero real é:", numero2, "\n")
print(f'seu número real é {numero2} \n')

#TIPO TEXTUAL - string
frase = input("Digite sua frase:")
#print("sua frase é: ", frase, "\n")
print(f'sua frase é {frase} \n')

#caso queira transformar uma variável é outra:
print(int(frase), "\n") #é um exemplo

#OPERAÇÕES MATEMÁTICAS
'''
Soma = +
Subtração = -
Multiplicação = *
Divisão = /
Divisão inteira = //
'''
numero01 = int(input("Digite o numero 01: "))
numero02 = int(input("Digite o numero 02: "))
soma = numero01 + numero02
#print("a soma é: ", soma,"\n" )
print(f'a soma é igual a {soma} \n')
subtracao = numero01 - numero02
#print("a subtracao é: ", subtracao,"\n" )
print(f'a subtracao é igual a {subtracao} \n')
multiplicacao = numero01 * numero02
#print("a multiplicação é: ", multiplicacao,"\n" )
print(f'a multiplicacao é igual a {multiplicacao} \n')
divisao = numero01 / numero02
#print("a divisão é: ", divisao,"\n" )
print(f'a divisao é igual a {divisao} \n')
divisaoInteira = numero01 // numero02
#print("a divisão inteira é: ", divisaoInteira,"\n" )
print(f'a divisão inteira é igual a {divisaoInteira} \n')