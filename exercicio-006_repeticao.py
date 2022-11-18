"""Faça um Programa que leia três números e mostre o maior deles."""

num_1 = int(input("digite um número! "))
num_2 = int(input("digite um segundo número! "))
num_3 = int(input("digite um terceiro número! "))

if num_1 > num_2 and num_1 >num_3:
    print("o maior número digitado é:", num_1)
elif num_2 > num_3 and num_2 >num_1:
    print("o maior número digitado é:", num_2)
elif num_3 > num_1 and num_3 < num_2:
    print("o maior número digitado é:", num_3)
        