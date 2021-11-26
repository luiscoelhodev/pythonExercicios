#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
maior = menor = 0
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in range(0, len(numeros)):
    if n == 0:
        maior = numeros[n]
        menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        elif numeros[n] < menor:
            menor = numeros[n]
    print(numeros[n], end=' ')
print(f'\nMaior número: {maior}')
print(f'Menor número: {menor}')



