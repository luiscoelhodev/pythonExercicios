#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para
# o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('-='*10)
print('Conversor de Bases')
print('-='*10)
numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n[1] Binário\n[2] Octal\n[3] Hexadecimal')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida!')

