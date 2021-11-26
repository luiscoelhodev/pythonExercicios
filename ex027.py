# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome: ').strip()
nome_lista = nome.split()
print('Prazer! Seu primeiro nome é "{}" e seu último nome é "{}".'.format(nome_lista[0], nome_lista[-1]))
