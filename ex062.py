#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contador = 1
acumulador = primeiro
sair = False
while not sair:
    if contador < 11:
        print('{} -> '.format(acumulador), end='')
        acumulador += razao
        contador += 1
    elif contador >= 11:
        print('PAUSA')
        quantos = int(input('Quantos termos ainda deseja mostrar? '))
        if quantos == 0:
            sair = True
        else:
            for c in range(0, quantos):
                print('{} -> '.format(acumulador), end='')
                acumulador += razao
                contador += 1
print('PA finalizada com {} termos mostrados!'.format(contador-1))

