# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numeros = []
posicoes_menor = []
posicoes_maior = []
for valor in range(0, 7):
    numeros.insert(valor, int(input('Digite um número inteiro: ')))
    if valor == 0:
        menor = numeros[valor]
        maior = numeros[valor]
    else:
        if numeros[valor] < menor:
            menor = numeros[valor]
        if numeros[valor] > maior:
            maior = numeros[valor]
for i in range(0, len(numeros)):
    if numeros[i] == menor:
        posicoes_menor.append(i+1)
    if numeros[i] == maior:
        posicoes_maior.append(i+1)
print(numeros)
print(f'O menor número digitado foi {menor} e apareceu nas posições: {posicoes_menor}')
print(f'O maior número digitado foi {maior} e apareceu nas posições: {posicoes_maior}')
