#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    numero = int(input('Tabuada de: '))
    if numero <= 0:
        print('Programa tabuada encerrado.')
        break
    for contador in range (0, 11):
        print(f'{numero} X {contador} = {numero*contador}')
    print('-='*10)

