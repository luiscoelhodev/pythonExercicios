# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da
# execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa
# deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
continuar = True
soma = 0
quantidade = 0
while continuar:
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    pergunta = input('Quer continuar? [S/N] ').strip().upper()[0]
    while pergunta != 'S' and pergunta != 'N':
        print('Você não digitou uma resposta válida! ')
        pergunta = input('Quer continuar? [S/N] ').strip().upper()[0]
    if pergunta == 'N':
        media = soma / quantidade
        print('A média dos números foi {:.2f}'.format(media))
        print('Menor número: {}\nMaior número: {}'.format(menor, maior))
        continuar = False