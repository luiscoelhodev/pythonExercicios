# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = list()
lista_pares = list()
lista_impares = list()
while True:
    numero = int(input('Digite um número: '))
    if numero not in lista:
        lista.append(numero)
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)
    else:
        print('Este número já foi inserido na lista anteriormente! ')
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
lista.sort()
lista_pares.sort()
lista_impares.sort()
print(f'Você digitou os valores: {lista}')
print(f'Os números pares foram: {lista_pares}')
print(f'Os números ímpares foram: {lista_impares}')
