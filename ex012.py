#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco_inicial = float(input('Preço do produto: '))
desconto = int(input('Porcentagem do desconto (%): '))

valor_final = preco_inicial - (preco_inicial * (desconto/100))

print('Seu produto de R${:.2f} com {}% de desconto custará R${:.2f}'.format(preco_inicial, desconto, valor_final))
