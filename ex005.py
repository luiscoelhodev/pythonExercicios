# Python Exercise 005: Make a program that reads an integer and show on the screen its successor and predecessor.

num = int(input('Digite um número qualquer: '))
print('Você digitou {}. \nSeu antecessor é {} e seu sucessor é {}.'.format(num, num-1, num+1))