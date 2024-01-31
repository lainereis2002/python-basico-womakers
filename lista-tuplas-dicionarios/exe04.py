'''crie um dicionário representando contatos (nome, telefone)
permita ao usuário procurar por um contato pelo nome'''

lista_telefonica = {
    'Gilmara': 81988484358,
    'Franklin': 81988484358,
    'Gislaine': 81988484358,
    'André': 81988484358,
    'Regina': 81988484358,
    'Davi': 81988484358,
    'Irene': 81988484358
}

contato = input("Digite o nome do contato: ")

if contato in lista_telefonica:
    print(f"Telefone de {contato}: {lista_telefonica[contato]} ")
else:
    print("Contato não encontrado, verifique se foi digitado corretamente com a primeira letra maiúscula e o resto minúscula. Caso sim, o contato não existe.")
