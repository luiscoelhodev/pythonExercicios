# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
# quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitorias = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 9)
    escolha = ' '
    while escolha not in 'PI':
        escolha = input('Par ou Ímpar? [P/I] ').upper().strip()[0]
    if escolha == 'P':
        if (computador + jogador) % 2 == 0:
            print(f'O computador jogou {computador} e você jogou {jogador}: Você venceu! ')
            vitorias += 1
        else:
            print(f'O computador jogou {computador} e você jogou {jogador}: Você perdeu! ')
            break
    elif escolha == 'I':
        if (computador + jogador) % 2 == 0:
            print(f'O computador jogou {computador} e você jogou {jogador}: Você perdeu! ')
            break
        else:
            print(f'O computador jogou {computador} e você jogou {jogador}: Você venceu! ')
            vitorias += 1
print(f'Game over! Você ganhou {vitorias} vezes consecutivas.')
