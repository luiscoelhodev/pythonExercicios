#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
total_idade = 0
mulheres_novas = 0
idade_velho = 0
homem_velho = ''
for pessoa in range(1, 5):
    print('== {}ª Pessoa =='.format(pessoa))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    if sexo == 'M':
        if idade > idade_velho:
            idade_velho = idade
            homem_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_novas += 1
    total_idade += idade
media = (total_idade / 4)
print('Média de idade do grupo: {} anos'.format(media))
print('Homem mais velho: {} - {} anos'.format(homem_velho, idade_velho))
print('{} mulheres com menos de 20 anos.'.format(mulheres_novas))
