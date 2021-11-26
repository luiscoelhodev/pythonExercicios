# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
contador = 0
nomes =[]
while contador < 4:
    nome = input('Digite o {}º nome: '.format(contador+1))
    nomes.append(nome)
    contador += 1
shuffle(nomes)
print('A nova ordem de apresentação será:', nomes)



