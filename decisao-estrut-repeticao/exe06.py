'''crie um progama que solicite ao usuário um login e uma senha
o programa deve permitir o acesso apenas se o usuário for "admin"
e a senha for "admin123", caso o contrário imprima uma mensagem de erro'''

usuario = "admin"
senha = "admin123"

login = input("Informe seu login: ")
password = input("Digite sua senha: ")

if login == usuario and password == senha:
    print("Usuário cadastrado, acesso liberado")
else:
    print("Usuário ou senha errados, acesso negado")