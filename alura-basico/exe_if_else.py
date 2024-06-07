# 1 Solicite ao usuário que insira um número e, em seguida, 
# use uma estrutura if else para determinar se o número é par ou ímpar.

def impar_ou_par():
    num = int(input("Digite um número inteiro: "))
    if (num%2 == 0):
        print(f"O número {num} é par\n")
    elif (num==0):
        print(f"O número {num} é neutro\n")
    else:
        print(f"O número {num} é ímpar\n")

#2 Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else 
# para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.
def classificacao_idade():
    idade = int(input("Digite a sua idade em anos: "))
    if (0<=idade<=12):
        print("Você é uma criança\n")
    elif (13<=idade<=18):
        print("Você é um adolescente\n")
    elif (idade<0):
        print("Idade inválida")
    else:
        print("Você é um adulto\n")

# 3 Solicite um nome de usuário e uma senha e use uma estrutura if else 
# para verificar se o nome de usuário e a senha fornecidos correspondem 
# aos valores esperados determinados por você.

def senha():
    usuario_correto = "alura"
    senha_correta = "alura123"

    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login bem sucedido!")
    else:
        print("Credenciais inválidas. Tente novamente.")


# 4 Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize 
# uma estrutura if elif else para determinar em qual quadrante do plano 
# cartesiano o ponto se encontra de acordo com as seguintes condições:
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem

def plano_cartesiano():
    x = float(input("Digite um valor para x: "))
    y = float(input("Digite um valor para y: "))
    
    if (x>0 and y>0):
        print("Esse ponto está localizado no 1º quadrante\n")
    elif (x<0 and y>0):
        print("Esse ponto está localizado no 2º quadrante\n")
    elif (x<0 and y<0):
        print("Esse ponto está localizado no 3º quadrante\n")
    elif (x>0 and y <0):
        print("Esse ponto está localizado no 4º quadrante\n")
    else:
        print("Esse ponto está localizado no eixo ou origem\n")    

def main():
    impar_ou_par()
    classificacao_idade()
    senha()
    plano_cartesiano()
    
if __name__ == '__main__':
    main()