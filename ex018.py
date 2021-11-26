# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
ang = float(input('Digite um ângulo, em graus: '))
rad = radians(ang)
print('Seno de {}: {:.2f}'.format(ang, sin(rad)))
print('Cosseno de {}: {:.2f}'.format(ang, cos(rad)))
print('Tangente de {}: {:.2f}'.format(ang, tan(rad)))

