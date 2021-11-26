# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
# em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
for i in range(0, 5):
    numero = int(input('Digite um número: '))
    if i == 0 or numero >= lista[-1]:
        lista.append(numero)
        print(f'Número {numero} adicionado à lista com sucesso! ')

    else:
        for n in range(0, len(lista)):
            if numero <= lista[n]:
                lista.insert(n, numero)
                print(f'Número {numero} adicionado na posição {n+1} da lista!')
                break
print(lista)
