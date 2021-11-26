numero = int(input('Fatorial de: '))
fatorial = 1
print('{}! = '.format(numero), end='')
for c in range(numero, 0, -1):
    if c > 1:
        print('{} x '.format(c), end='')
    else:
        print('1 = ', end='')
    fatorial = fatorial * c
print(fatorial)

