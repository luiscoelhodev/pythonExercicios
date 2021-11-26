#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
# elas podem ou não formar um triângulo.
a = float(input('Digite o valor do 1º segmento: '))
b = float(input('Digite o valor do 2º segmento: '))
c = float(input('Digite o valor do 3º segmento: '))
if (b-c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Os lados informados podem formar um triângulo!')
else:
    print('Os lados informados NÃO podem formar um triângulo! ')

