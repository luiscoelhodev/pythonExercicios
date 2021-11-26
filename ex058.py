#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
print('Olá, sou seu computador!\nPensei num número de 0 a 10 e gostaria que você tentasse adivinhar.')
computador = randint(0, 10)
tentativas = 1
numero = int(input('Seu palpite: '))
while numero != computador:
    if numero < 0 or numero > 10:
        print('O seu palpite deve ser de 0 a 10... ', end='')
        numero = int(input('Tente novamente: '))
        tentativas += 1
    else:
        if numero > computador:
            print('Menos... ', end='')
            numero = int(input('Tente novamente: '))
            tentativas += 1
        elif numero < computador:
            print('Mais... ', end='')
            numero = int(input('Tente novamente: '))
            tentativas += 1
print('Parabéns! Você tentou {} vezes.'.format(tentativas))
