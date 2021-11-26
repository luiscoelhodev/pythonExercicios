#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contador = 1
acumulador = primeiro
while contador <= 10:
    print('{}'.format(acumulador), end='')
    if contador < 10:
        print(' -> ', end='')
    else:
        print('')
    acumulador += razao
    contador += 1
