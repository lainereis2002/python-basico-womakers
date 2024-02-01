'''crie uma função chamada contar_vogais que recebe uma string como parametro
implemente a lógica para conta o número de vogais na string e retorne o total
de vogais. Solicie ao usuário para inserie uma frase e utilize a função para
contar as vogais'''

def contar_vogais(frase):
    vogais = set("aeiouAEIOU")
    cont = 0

    for alfabeto in frase:
        if alfabeto in vogais:
            cont+=1
    
    print(f"{cont} vogais na frase {frase}")



frase = input("Digite uma frase ou palavra: ") 
contar_vogais(frase)