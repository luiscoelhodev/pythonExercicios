num = int(input('Digite um número: '))
print('=== Tabuada de {} ==='.format(num))

for contador in range(0, 11):
    print('{:2} x {:2} = {:2}'.format(num, contador, num*contador))
