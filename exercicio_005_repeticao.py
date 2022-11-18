"""Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez."""

nota_01 =float(input("Digite a primeira nota! "))
nota_02 = float(input("Digite a segunda nota! "))

media = round((nota_01 + nota_02) / 2 , 2)

print(media)

if float (media >=7) and media < 10:
    print("APROVADO")
elif float (media < 7):
    print("REPROVADO")
elif media == 10:
    print("Aprovado com Distinção")
