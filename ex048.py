# Exercício Python 048: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de
# três e que se encontram no intervalo de 1 até 500.
soma = 0
total = 0
for contador in range(1, 501):
    if contador % 2 != 0 and contador % 3 == 0: #somente os números ímpares múltiplos de 3
        soma += contador
        total += 1
print('A soma dos {} números é {}.'.format(total, soma))

