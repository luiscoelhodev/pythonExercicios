# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
contador = 0
nomes = []

while contador <4: #Este while fará com quem os nomes digitados sejam adicionados à lista vazia criada acima.
    nome = input('Digite um nome: ')
    nomes.append(nome) #Usa esse comando append para adicionar nomes ao final da lista
    contador += 1

selecionado = choice(nomes)

# OU selecionado = randint(0, 4) #Gera um numero entre 0 e 3

print('O nome selecionado foi {}!'.format(selecionado)) #Printa o nome correspondente ao índice gerado
