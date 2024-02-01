def multiplicacao():
    mult = 10*2
    file = 'arquivo.txt'

    #abertura de arquivo
    arquivoLeitura = open(file, "r") #open apenas para leitura
    arquivoEscrita = open(file, "w") #open apenas para escrita
    #arquivoBinario = open(file, "wb") #open de arquivos binários (zeros e uns)

    #escrita
    arquivoEscrita.write("Texto a ser escrito")
    arquivoEscrita.close() #fechando o arquivo

    #leitura
    leitura = arquivoLeitura.read()
    print(leitura) #printando no terminal
    arquivoLeitura.close() #fechando o arquivo

    print(f"O resultado da multiplicação é: {mult}")
    
multiplicacao()