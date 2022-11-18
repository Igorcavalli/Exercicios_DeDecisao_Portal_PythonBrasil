"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""



sexo = input("digite a letra (M) para Masculino ou (F) para Feminino ").upper()

if sexo == "M":
    print("seu sexo é Masculino")
elif sexo =="F":
    print(" seu sexo é Feminino")
else:
    print ("sexo inválido")

