# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a
# letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
#Usando a função 'rfind', a busca é feita da direita pra esquerda(trás pra frente)!

frase = input('Digite uma frase: ').strip()
quantos_a = frase.lower().count('a')
print('A letra "a" aparece {} vezes.'.format(quantos_a))
print('A primeira vez que ela aparece é na posição {}.'.format(frase.lower().find('a')))
print('A última vez que ela aparece é na posição {}.'.format(frase.lower().rfind('a')))

