# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com
# o nome "SANTO".
cidade = input('Digite o nome da sua cidade: ').strip()
cidade_lista = cidade.split()
if cidade_lista[0].lower() == 'santo':
    print('O nome dessa cidade começa com "Santo"! ')
else:
    print('O nome dessa cidade NÃO começa com "Santo"!')
