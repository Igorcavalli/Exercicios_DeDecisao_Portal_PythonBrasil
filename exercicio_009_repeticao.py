"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""

lista = []

for numero in range(3):
    numero = int(input(f'Entre com o número {numero + 1} '))
    lista.append(numero)
print()
lista.sort(reverse = True)
print(lista)