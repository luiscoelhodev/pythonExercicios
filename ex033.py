#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
numeros = [n1, n2, n3]
maior = n1
menor = n2
for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print('O maior número é {} e o menor é {}'.format(maior, menor))
