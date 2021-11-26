# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
brasileirao = ('Flamengo', 'Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Corinthians', 'International',
               'Athlético-PR', 'Fluminense', 'América-MG', 'Atlético-GO', 'Cuiabá', 'São Paulo', 'Ceará',
               'Juventude', 'Santos', 'Bahia', 'Sport', 'Grêmio', 'Chapecoense')
chapeco = brasileirao.index('Chapecoense')
print(f'Lista dos times do Brasileirão Série A: {brasileirao}')
print(f'Os 5 primeiros colocados: {brasileirao[0:5]}')
print(f'Os 4 últimos colocados: {brasileirao[-4:]}')
print(f'Em ordem alfabética: {sorted(brasileirao)}')
print(f'Posição da Chapecoense: {chapeco + 1}º')



