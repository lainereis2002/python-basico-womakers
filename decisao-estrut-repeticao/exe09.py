'''o programa deve alcular e apresentar a quantidade de números pares
e impares inseridos. O processo de leitura deve ser encerrado quando 
o usuário informa o valor zero. Certifique-se de incluir validações
para garantir que apenas número positivos sejam considerados na 
contagem e cálculos'''
contImpar = 0
contPar = 0
while True:
    numero = int(input("Digite um numero positivo: "))
    if numero > 0:
        if numero%2 == 0:
            contPar+=1
        else:
            contImpar+=1
    elif numero == 0:
        break
    else:
        print("Números negativos não podem ser inseridos")

print(f"Contagem de número pares: {contPar}")
print(f"Contagem de números ímpares: {contImpar}")