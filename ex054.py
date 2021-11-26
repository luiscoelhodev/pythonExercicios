#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year
maiores = 0
menores = 0
for c in range(0, 7):
    nascimento = int(input('Ano de nascimento da {}ª pessoa: '.format(c+1)))
    if (ano_atual - nascimento) >= 18:
        maiores += 1
    else:
        menores += 1
print('Dessa lista, {} pessoas são maiores e {} são menores.'.format(maiores, menores))
