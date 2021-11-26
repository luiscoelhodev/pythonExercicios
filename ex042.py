#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (b-c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Os lados podem formar um triângulo', end=' ')
    if a != b != c != a:
        print('escaleno.')
    elif a == b != c or a == c != b or b == c != a:
        print('isósceles.')
    elif a == b == c:
        print('equilátero.')
else:
    print('Os lados não podem formar um triângulo!')
