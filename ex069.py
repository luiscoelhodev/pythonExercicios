# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
total_pessoas = total_homens = mulheres_20 = total_18 = 0

while True:
    print('\n', '-='*4, 'Cadastro de Pessoas', '-='*4)
    idade = int(input('Idade deste indivíduo: '))
    if idade < 0:
        while idade < 0:
            print('Idade não pode ser menor que 0! ')
            idade = int(input('Idade deste indivíduo: '))
    sexo = input('Sexo desta pessoa: [M/F] ').strip().upper()[0]
    while sexo not in 'MF':
        print('Escolha Masculino (M) ou Feminino (F)! ')
        sexo = input('Sexo desta pessoa: [M/F] ').strip().upper()[0]
    total_pessoas += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1
    if idade > 18:
        total_18 += 1
    continuar = input('\nDeseja continuar? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        print('\nEscolha uma opção válida! (S ou N)')
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'Cadastro encerrado.\nForam cadastradas {total_18} pessoas maiores de 18 anos, {total_homens} homens e {mulheres_20} mulheres com menos de 20 anos.')
print(f'Total de pessoas: {total_pessoas}')
