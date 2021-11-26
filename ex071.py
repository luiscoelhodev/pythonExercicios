#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte
# ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
valor = int(input('Valor a ser sacado: R$'))
notas_50 = valor // 50
resto_50 = valor % 50
notas_20 = resto_50 // 20
resto_20 = resto_50 % 20
notas_10 = resto_20 // 10
resto_10 = resto_20 % 10
notas_1 = resto_10
print(notas_50, notas_20, notas_10, notas_1)
