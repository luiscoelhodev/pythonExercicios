# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a
# sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo
# do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Em que ano você nasceu? '))
sexo = input('Qual o seu sexo? (M ou F): ').strip().upper()
idade = ano_atual - ano_nascimento
print('Quem nasceu em {} como você hoje tem {} anos.'.format(ano_nascimento, idade))
if idade < 18 and sexo == 'M':
    print('Faltam {} anos para o seu alistamento!'.format(18-idade))
    print('Seu alistamento será em {}'.format(18-idade + ano_atual))
elif idade == 18 and sexo == 'M':
    print('Este é o ano para você se alistar!')
elif idade > 18 and sexo == 'M':
    print('Já se passaram {} anos do seu alistamento.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(ano_atual - (idade-18)))
elif sexo == 'F':
    print('Você é mulher e não tem obrigatoriedade de se alistar.')
else:
    print('Sexo inválido!')

