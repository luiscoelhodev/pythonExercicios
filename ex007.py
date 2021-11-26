# Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

num1 = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segunda nota: '))
media = (num1+num2)/2

print('A média entre {:.1f} e {:.1f} é {:.1f}.'.format(num1, num2, media))