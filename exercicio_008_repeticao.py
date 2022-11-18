"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato."""

p1 = float(input("Insira o preço do Produto! R$ "))
p2 = float(input("Insira o preço do segindo produto! R$ " ))
p3 = float(input("Insira o preço do terceiro produto! R$ "))

valor = [p1, p2, p3]

menor_valor = print("O produto que apresenta o menor preço é: R$", min(valor))