#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
numero = int(input('Digite um número para saber seu fatorial: '))
contador = numero
fatorial = 1
print('Calculando {}! --> '.format(numero), end='')
while contador > 0:
    print('{} '.format(contador), end='')
    print('x ' if contador > 1 else '= ', end='')
    fatorial = fatorial * contador
    contador -= 1
print(fatorial)
