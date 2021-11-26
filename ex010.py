#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Digite seu dinheiro em BRL: '))
dolar = real * 0.19

print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))
