#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
computador = randint(0, 6)
print('-='*18)
print('Jogo da adivinhação v1.0')
print('-='*18)
jogador = int(input('Digite um número inteiro entre 0 e 5: '))
print('Eu pensei em {} e você digitou {}.'.format(computador, jogador))
if computador == jogador:
    print('Parabéns! Você venceu.')
else:
    print('Que pena! Tente novamente depois.')
