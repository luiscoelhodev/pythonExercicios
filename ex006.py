# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número: '))
print('Você digitou {}.'.format(num))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('Seu dobro: {}\nSeu triplo: {} \nSua raiz quadrada: {}'.format(dobro, triplo, raiz))
