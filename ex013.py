#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario_inicial = float(input('Salário inicial: '))
aumento = int(input('Aumento(%): '))
novo_salario = salario_inicial + (salario_inicial*(aumento/100))

print('Salário atualizado de R${:.2f} para R${:.2f} com {}% de aumento.'.format(salario_inicial, novo_salario, aumento))
