#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = input('Digite uma frase: ').strip().upper()
frase_lista = frase.split()
frase_sem_espacos = ''.join(frase_lista)
inverso_lista = []
for letra in frase_sem_espacos:
    inverso_lista.insert(0, letra)
inverso = ''.join(inverso_lista)
print('{} ao contrário é {}.'.format(frase_sem_espacos, inverso))
if frase_sem_espacos == inverso:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')


