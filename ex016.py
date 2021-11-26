# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc

num_float = float(input('Digite um número real: '))
num_int_trunc = trunc(num_float) #Primeiro jeito de se fazer, usando o método trunc da biblioteca math
num_int = int(num_float) #Segundo jeito de fazer convertendo o número para inteiro
print('Você digitou {}, sua porção inteira é {}'.format(num_float, num_int))

print(num_int_trunc)