# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
# se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
total = produtos_1000 = contador = preco_barato = 0
while True:
    nome = input('Nome do produto: ').strip()
    preco = float(input('Preço: R$'))
    if contador == 0:
        nome_barato = nome
        preco_barato = preco
    elif contador > 0:
        if preco < preco_barato:
            nome_barato = nome
    total += preco
    if preco > 1000:
        produtos_1000 += 1
    contador += 1
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        print('Por favor, digite S ou N! ')
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print('Compra finalizada.')
print(f"Total: R${total:.2f}\n{produtos_1000} produtos custam mais de R$1000.\nProduto mais barato: {nome_barato}")
