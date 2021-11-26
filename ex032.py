#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Digite o ano para verificação (0 para o ano atual) : '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    if ano % 400 == 0:
        print('O ano {} é bissexto!'.format(ano))
    else:
        print('O ano {} NÃO é bissexto!'.format(ano))

