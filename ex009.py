#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

contador = 0
num = int(input('Digite um número: '))
print('=== Tabuada de {} ==='.format(num))

while contador <= 10:
    print('{} x {} = {}'.format(num, contador, num*contador))
    contador += 1

