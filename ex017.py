# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = (co**2 + ca**2)**(1/2) # Primeiro jeito de fazer: cálculo matemático

hip = hypot(co, ca) # Segundo jeito de fazer: através da função hypot da biblioteca math
print(hip)

print('A hipotenusa vale {:.2f}'.format(h))
