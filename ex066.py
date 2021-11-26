# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre elas (desconsiderando o flag).
quantidade = soma = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    quantidade += 1
    soma += numero
print(f'Você digitou {quantidade} números e a soma entre eles foi {soma}.')

