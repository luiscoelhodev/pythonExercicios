# Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
# de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for counter in range (10, 0, -1):
    print(counter)
    sleep(0.5)
print('\U0001F4A5', '\U0001F389', '\U00002728')