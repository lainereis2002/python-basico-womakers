'''vamos construir um jogo da forca
o prgrama escolherá aleatoriamente a palavra secreta de uma lista predifinida
a palavra secreta sera representada por espaços em branco
um para cada letra da palavra
o jogador tera um numero limitado de 6 tentativas
em cada tentativa, o jogador pode fornecer uma letra
se a letra estiver presente na palavra secreta, ela será revelada nas posições certas
se a letra n estiver na palavra, uma mensagem de erro deverá ser mostrada
após um numero maximo de erros, o jogador perde
o jogo continua ate que o jogador adivinhe a palavra ou exceda o numero maximo de tentativas
dica: vc precisara importar uma biblioteca para resolver esse exercício'''

import random
vidas = 6
lista = ("BANANA", "MACA", "MARACUJA", "GOIABA", "LARANJA")
palavra_sorteada = random.choice(lista)
digitadas = []
ganhou = False

while True:
    print("\n")
    for letra in palavra_sorteada:
        if letra in digitadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    letra = input("\nDigite uma letra: ").upper()
    digitadas.append(letra)

    if len(letra)>1:
        print("ERROR: apenas uma letra por vez pode ser digitada")
        continue

    if letra not in palavra_sorteada:
        vidas -= 1
        print(f"Você tem {vidas} vidas restantes")

    ganhou = all(letra in digitadas for letra in palavra_sorteada)

    if vidas == 0 or ganhou:
        break

if ganhou:
    print(f"\nParabéns, você ganhou!!! A palavra era {palavra_sorteada}")
else:
    print(f"\nVocê perdeu :( a palavra era {palavra_sorteada}")



