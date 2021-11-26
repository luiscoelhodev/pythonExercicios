# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('='*20)
print('{:^20}'.format('Jokenpô'))
print('='*20)
print('''[1] Pedra
[2] Papel
[3] Tesoura''')
jogador = int(input('Qual a sua opção? '))
if jogador != 1 and jogador != 2 and jogador != 3:
    print('Opção inválida!')
else:
    computador = randint(1, 3)
    print('Jo')
    sleep(0.5)
    print('Ken')
    sleep(0.5)
    print('Pô!')
    print('Você jogou {} e o computador jogou {}.'.format(itens[jogador-1], itens[computador-1]))
    if jogador == computador:
        print('Empate!')
    elif jogador == 1 and computador == 2:
        print('Você perdeu!')
    elif jogador == 1 and computador == 3:
        print('Você venceu!')
    elif jogador == 2 and computador == 1:
        print('Você venceu!')
    elif jogador == 2 and computador ==3:
        print('Você perdeu!')
    elif jogador == 3 and computador == 1:
        print('Você perdeu!')
    elif jogador == 3 and computador == 2:
        print('Você venceu!')

