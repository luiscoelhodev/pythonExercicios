# Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

variavel = input('Digite qualquer coisa: ')

if variavel.isalpha():
    print('O que você digitou é só letras.')
if variavel.isnumeric():
    print('O que você digitou é só números.')
if variavel.islower():
    print('O que você digitou está tudo em letras minúsculas.')
if variavel.istitle():
    print('O que você digitou começa com letra maiúscula.')
if variavel.isupper():
    print('O que você digitou está em caixa alta!')
if variavel.isspace():
    print('Você só digitou espaços!')
