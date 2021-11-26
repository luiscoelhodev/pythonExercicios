#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
divisivel = 0
numero = int(input('Digite um número: '))
for counter in range(1, numero+1):
    if numero % counter == 0:
        print('\033[1;33m{}\033[m'.format(counter), end=' ')
        divisivel += 1
    else:
        print('\033[1;31m{}\033[m'.format(counter), end=' ')
print('\nO número {} foi divisível {} vezes. \nPor isso, '.format(numero, divisivel), end='')
if divisivel == 2:
    print('ele é primo!')
else:
    print('ele não é primo!')




