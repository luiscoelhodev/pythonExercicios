# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lápis', 1, 'Borracha', 0.5, 'Caderno', 10, 'Caneta', 2, 'Estojo', 10, 'Mochila', 119.90, 'Livro', 39.99)
print('-'*40)
print(f'{"Tabela de Preços":^40}')
print('-'*40)
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<30}', end='')
    else:
        print(f'R${produtos[i]:>7.2f}')
