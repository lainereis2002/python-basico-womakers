from funcoes_do_log import * #o * é para importar tudo (mas não é uma boa prática)
# tudo o que tem nesse namespace é importado para cá
# não é uma boa prática pois nem sempre é usado TUDO de outro módulo

imprimir_no_log(f"Bem vinda, {nome_de_usuario}")
# não foi necessário colocar o funcoes_do_log. pois ele já importou tudo
#ou seja não precisa mais definir