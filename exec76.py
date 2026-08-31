'''
CRIE UM PROGRAMA QUE TENHA UMA TUPLA UNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS SA SEQUENCIA.
NO FINAL, MOSTRE UMA LISTA DE PREÇOS ORGANIZADO OS DADOS EM FORMA TABULA
'''

tupla = (
    ('PS 5', 3500.00), 
    ('GTA 6', 540.00), 
    ('Salgadinho', 12.50))

print(f'{'PRODUTO':<20} | {'PREÇO':<5}')
print("-"*46)

for nome, preco in tupla:
    print(f'{nome:.<35}R$ {preco:>7.2f}')