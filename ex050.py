#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
# que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
pares = 0
quantos = int(input('Quantos números você quer digitar? '))
for contador in range(0, quantos):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        soma += numero
        pares += 1
print('Você digitou {} números pares e a soma foi {}.'.format(pares, soma))
