#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o
# seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
total = float(input('Total das compras: R$'))
print('=== Formas de Pagamento ===')
print('[1] À Vista no dinheiro/cheque - 10% de desconto')
print('[2] À Vista no cartão - 5% de desconto')
print('[3] Em até 2x no cartão - preço normal')
print('[4] Em 3x ou mais no cartão - 20% de Juros')
opcao = input('Qual sua opção? ')
if opcao == '1':
    preco_final = total*0.9
    print('Sua compra de R${:.2f} com 10% de desconto à vista sairá a R${:.2f}'.format(total, preco_final))
elif opcao == '2':
    preco_final = total*0.95
    print('Sua compra de R${:.2f} com 5% de desconto à vista no cartão sairá a R${:.2f}'.format(total, preco_final))
elif opcao == '3':
    parcelas = total / 2
    print('Sua compra de R${:.2f} sairá em 2x de R${:.2f}'.format(total, parcelas))
elif opcao == '4':
    quantidade_parcelas = input('Quantas parcelas deseja? ')
    if quantidade_parcelas.isnumeric() == False:
        print('Você deveria ter digitado num número! ')
    else:
        quantidade_parcelas_int = int(quantidade_parcelas)
        if quantidade_parcelas_int < 3:
            print('Volte a operação e selecione outra opção no menu inicial! ')
        else:
            preco_juros = total * 1.2
            parcelas = preco_juros / quantidade_parcelas_int
            print('Você pagará juros de 20%. Sua compra de R${:.2f} sairá por R${:.2f} em {}x de R${:.2f}'.format(total, preco_juros, quantidade_parcelas, parcelas))
else:
    print('Opção inválida! ')
