# Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
while True: #Loop infinito que será quebrado caso um dos 'if' seja atendido
    numero = input('Digite um número entre 0 e 9999: ').strip()
    numero_int = int(numero) #Converter o numero que é string para int para verificar no while a seguir
    while numero_int < 0 or numero_int > 9999: #Impede que o usuário não respeite o limite pedido
        numero = input('Digite um número entre 0 e 9999: ').strip()
        numero_int = int(numero)
    if len(numero) == 1:
        print('Unidade: {}'.format(numero))
        print('Dezena: 0')
        print('Centena: 0')
        print('Milhar: 0')
    elif len(numero) == 2:
        print('Unidade: {}'.format(numero[1]))
        print('Dezena: {}'.format(numero[0]))
        print('Centena: 0')
        print('Milhar: 0')
    elif len(numero) == 3:
        print('Unidade: {}'.format(numero[2]))
        print('Dezena: {}'.format(numero[1]))
        print('Centena: {}'.format(numero[0]))
        print('Milhar: 0')
    elif len(numero) == 4:
        print('Unidade: {}'.format(numero[3]))
        print('Dezena: {}'.format(numero[2]))
        print('Centena: {}'.format(numero[1]))
        print('Milhar: {}'.format(numero[0]))
    break
