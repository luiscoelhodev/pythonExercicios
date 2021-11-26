# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos
# todos os valores únicos digitados, em ordem crescente.
lista = []
contador = 0
contador_for = 0
while True:
    adicionado = int(input('Digite um número para inserir na lista: '))
    if contador == 0:
        lista.append(adicionado)
        print(f'Número {adicionado} adicionado com sucesso!')
    else:
        for numero in range(0, len(lista)):
            if adicionado == lista[numero]:
                contador_for += 1
        if contador_for > 0:
            print(f'O número {adicionado} já se encontra na lista e por isso não será adicionado novamente.')
        else:
            lista.append(adicionado)
            print(f'Número {adicionado} adicionado com sucesso!')
    contador += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Desejar continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'Os números digitados foram: {sorted(lista)}')





