#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1) * razao
for contador in range(primeiro, decimo + razao, razao):
    print(contador, end=' -> ')
print('ACABOU')
