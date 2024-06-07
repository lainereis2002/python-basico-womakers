# 1 Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ["Gilmara", "Franklin", "Irene", "Davi"]
nasc = [2002, 2024]

#2 Crie uma lista e utilize um loop for 
# para percorrer todos os elementos da lista. 
def loop_percorrer():
    for numeros in num:
        print(numeros)

#3 Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
def somar_impares():
    impar = 0
    for numero in num:
        if numero%2 != 0:
            impar = impar + numero
    
    print(f"A soma dos impares é igual a {impar}")

#4 Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
def loop_decrescente():
    num.sort(reverse=True)
    print(num)

# 5 Solicite ao usuário um número e, em seguida, utilize um loop for 
# para imprimir a tabuada desse número, indo de 1 a 10.
def tabuada():
    numero = float(input("Digite um número: "))
    for i in range(10):
        print(f"{numero} x {i+1} = {numero * (i+1)}")

# 6 Crie uma lista de números e utilize um loop for para calcular a 
# soma de todos os elementos. Utilize um bloco try-except para lidar 
# com possíveis exceções.
def soma_todos_numeros():
    soma = 0
    try:
        for numero in num:
            soma += numero
            
        print(f"A soma dos números {num} é = {soma}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    

# 7 Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, 
# caso a lista esteja vazia.
def media():
    soma = 0
    try:
        for numero in num:
            soma += numero
        media = soma/len(num)
        print(f"A media de {num} é = {media}")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero")

def main():
    loop_percorrer()
    somar_impares()
    loop_decrescente()
    tabuada()
    soma_todos_numeros()
    media()
    
if __name__ == '__main__':
    main()