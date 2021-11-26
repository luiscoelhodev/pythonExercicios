# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = float(input('Digite um valor em metros: '))
print('{}m equivale a:\n{} Km\n{} Hem\n{} Dam\n{} dm\n{} cm\n{} mm'.format(metros, metros*0.001, metros*0.01, metros*0.1, metros*10, metros*100, metros*1000))
