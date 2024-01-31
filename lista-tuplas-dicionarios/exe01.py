'''utilizando listas faça um programa que faça 5 perguntas 
para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?" 
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões, "Suspeita"
entre 3 e 4, "Cumplice", e 5 como "Assassino"
caso contrário, ele será classificado como "Inocente"
'''
respostas = []
r1 = input("Telefonou para a vítima? R: ").upper()
r2 = input("Esteve no local do crime? R: ").upper()
r3 = input("Mora perto da vítima? R: ").upper()
r4 = input("Já trabalhou com a vítima? R: ").upper()
r5 = input("Devia para a vítima? R: ").upper()
respostas.extend([r1, r2, r3, r4, r5])

if respostas.count("SIM") == 2:
    print("Suspeita")
elif respostas.count("SIM") == 3 or respostas.count("SIM") == 4:
    print("Cúmplice")
elif respostas.count("SIM") == 5:
    print("Assassino")
else:
    print("Inocente") 