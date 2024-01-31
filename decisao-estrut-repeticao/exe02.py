'''faça um prpograma que pergunte o turno que voce estuda
peça p digitar:
M - matutino
V - verpertino
N - noturno
imprima a mensagem bom dia, boa tarde, boa noite ou valor inválido'''

print("M - matutino \nV - verpertino \nN - noturno ")
turno = input("Digite o turno o qual vc estuda: ").upper()

if turno == 'M':
    print("Bom dia!")
elif turno == 'V':
    print("Boa tarde!")
elif turno == 'N':
    print("Boa noite!")
else:
    print("Valor inválido")