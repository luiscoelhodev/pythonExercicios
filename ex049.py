# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
numero = int(input('Digite um número para saber sua tabuada: '))
for contador in range (0, 11):
    print('{} x {:2} = {:2}'.format(numero, contador, numero*contador))
