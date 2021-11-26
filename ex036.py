#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal
# não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Seu salário: R$'))
anos = int(input('Anos a pagar: '))
prestacao = valor_casa / (anos*12)

if prestacao > salario * 0.3:
    print('O valor da prestação é R${:.2f}. Ele é maior que 30% do seu salário. Infelizmente, você não pode comprá-la.'.format(prestacao))
else:
    print('Você pagará o valor de R${:.2f} em {} anos.'.format(valor_casa, anos))
    print('Valor mensal: R${:.2f}'.format(prestacao))
