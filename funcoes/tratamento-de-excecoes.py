def divisao(a, b):
    try: #tente
        resultado = a/b
        print(resultado)
    #exceções
    except ZeroDivisionError:
        print("Erro: Impossível dividir um valor por zero")
    except TypeError as e:
        print(f"Erro: o tipo do dado informado está incorreto.\nDetalhes: {e}")
    else:
        print("Sem exceções")


divisao(10, 2) #funciona
#divisao(10, 0) #ZeroDivisionError
#divisao(10, "womakerscode") #TypeError
    