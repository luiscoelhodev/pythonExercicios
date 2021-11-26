#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Digite a temperatura em ºC: '))
fahrenheit = (celsius * 1.8) + 32
print('{}ºC equivale a {:.1f}ºF'.format(celsius, fahrenheit))