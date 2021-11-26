# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
tupla = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
contador = 0
print(f'Os valores digitados foram: {tupla}')
if 9 in tupla:
    print(f'O número 9 apareceu {tupla.count(9)} vezes. ')
else:
    print('O valor 9 não apareceu nesta tupla!')
if 3 in tupla:
    print(f'O primeiro valor 3 apareceu na {tupla.index(3)+1}ª posição. ')
else:
    print('O valor 3 não está nesta tupla! ')
for n in tupla:
    if n % 2 == 0:
        contador += 1
        if contador == 1:
            print('Os valores pares são: ', end='')
            print(n, end=' ')
        else:
            print(n, end=' ')
if contador == 0:
    print('Não há números pares nesta tupla!')


