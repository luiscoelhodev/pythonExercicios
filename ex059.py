# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
from time import sleep
sair = False
numero1 = float(input('Primeiro número: '))
numero2 = float(input('Segundo número: '))
while not sair:
    print('''O que você deseja fazer com eles?
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        soma = numero1 + numero2
        print('A soma entre {} e {} é {}.'.format(numero1, numero2, soma))
    elif opcao == 2:
        produto = numero1 * numero2
        print('O produto entre {} e {} é {}.'.format(numero1, numero2, produto))
    elif opcao == 3:
        if numero1 > numero2:
            print('{} é maior que {}'.format(numero1, numero2))
        elif numero2 > numero1:
            print('{} é maior que {}'.format(numero2, numero1))
        else:
            print('Os números são iguais!')
    elif opcao == 4:
        print('Vamos lá novamente...')
        numero1 = float(input('Primeiro número: '))
        numero2 = float(input('Segundo número: '))
    elif opcao == 5:
        sair = True
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida! ')