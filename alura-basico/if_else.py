import os

restaurantes = [{"nome": "Praça", "categoria": "Japonesa", "ativo": False},
                {"nome": "Pizza Suprema", "categoria": "Italiana", "ativo": True},
                {"nome": "Lalis", "categoria": "Árabe", "ativo": False}]

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_programa():
    exibir_subtitulo("Finalizando Programa...")

def voltar_ao_menu():
    input ("\nDigite uma tecla para voltar ao menu principal ")
    main()

def opcao_invalida():
    print("\nOpção inválida")
    voltar_ao_menu()
    
def exibir_subtitulo(texto):
    os.system("cls")
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo": False}
    
    restaurantes.append(dados_do_restaurante)
    print(f"O resurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes")
    
    print(f"{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}")
    
    voltar_ao_menu()

def alternar_estado_restaurante():
    exibir_subtitulo("Alterando estado do restaurante")
    
    nome_restaurante = input("Digite o nome do restauramte que deseja alterar o estado: ")
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")
    
    voltar_ao_menu()

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    print(f'Você escolheu a opção {opcao_escolhida}')

    try:
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante() #print('Cadastrar restaurante')
        elif opcao_escolhida == 2:
            listar_restaurantes() #print('Listar restaurante')
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    
def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()