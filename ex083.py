# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = input('Digite uma expressão aritmética com parênteses: ')
lista = []
parenteses_abertos = 0
parenteses_fechados = 0
for i in expressao:
    if i == '(' or i == ')':
        lista.append(i)
for c in range(0, len(lista)):
    if c == 0 and lista[c] == ')':
        print('Expressão começa com ")": não é válida! ')
    if lista[-1] == '(':
        print('Expressão termina com "(": não é válida! ')
        break
    if lista[c] == '(':
        parenteses_abertos += 1
    if lista[c] == ')':
        parenteses_fechados += 1
        if parenteses_fechados > parenteses_abertos:
            print('Expressão inválida por fechar mais parenteses do que que abrir!')
            break
print(lista)
print(parenteses_abertos)
print(parenteses_fechados)
if parenteses_abertos != parenteses_fechados:
    print('Expressão inválida! ')



