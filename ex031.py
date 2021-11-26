#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input('Qual a distância da viagem (em Km)? '))
if distancia < 200:
    custo = distancia * 0.5
else:
    custo = distancia * 0.45
print('A sua viagem custará R${:.2f}'.format(custo))
