# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
quantos = 0
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    quantos += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
lista.sort(reverse=True)
print(lista)
print(f'Foram digitados {quantos} números.')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 NÃO está na lista!')


