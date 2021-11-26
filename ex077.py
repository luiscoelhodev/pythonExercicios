# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Praticar', 'Trabalhar', 'Futuro', 'Mercado')
vogais = ('a', 'e', 'i', 'o', 'u')
for palavra in range(0, len(palavras)):
    string = palavras[palavra]
    print(f'\nA palavra "{string}" tem as seguintes vogais: ', end='')
    for letra in string:
        for vogal in vogais:
            if letra.lower() == vogal:
                print(letra.upper(), end=' ')



