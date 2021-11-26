# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome: ').strip()
print('Analisando o seu nome...')
print('Nome em letras maiúsculas: {}'.format(nome.upper()))
print('Nome em letras minúsculas: {}'.format(nome.lower()))
nome_lista = nome.split()
nome_sem_espacos = ''.join(nome_lista)
print('O seu nome tem {} letras.'.format(len(nome_sem_espacos)))
print('O seu primeiro nome é {} e ele tem {} letras.'.format(nome_lista[0], len(nome_lista[0])))

