# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
infos = {"nome": "Gislaine",
         "idade": 21,
         "cidade": "Recife"}

# 2 - Utilizando o dicionário criado no item 1:
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
infos.update({"idade": 22})
# Adicione um campo de profissão para essa pessoa;
infos.update({"profissão": 'estagiária'})
# Remova um item do dicionário.
del infos['cidade']
#print(infos)

# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
quadrados = {'1': 1*1,
             '2': 2*2,
             '3': 3*3,
             '4': 4*4,
             '5': 5*5}
#print(quadrados)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
existe = 'existe' if infos['nome'] else 'não existe'
#print(existe)

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
def frequencia(lista):
    freq_palavras = {palavra: lista.count(palavra) for palavra in lista}
    return(freq_palavras)

lista = ["eu", "estou", "vivendo", "um", "dos", "dias", "mais", "tristes", "da", "minha", "vida",
         "acho", "que", "nunca", "me", "senti", "tão", "triste", "acho", "que", "nunca", "tive",
         "um", "dia", "tão", "triste"]

print(frequencia(lista))