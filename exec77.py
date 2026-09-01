'''
CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VARIAS PALAVRAS (NÃO USAR ACENTOS).
DEPOIS DISSO, VOCÊ DEVE MOSTRAR PARA CADA PALAVRA, QUAIS SÃO AS SUAS VOGAIS.
'''

print('==='*15)
print('EXERCICIOS 77'.center(45))
print('==='*15)
print(' ')

tupla = ('uva', 'sapo', 'sapato', 'tabiada', 'acidos', 'cavalo','topete', 'tonto', 'morcego', 'ovelha')
vogais = 'aeiou'

for palvra in tupla:
    print(f'Em {palvra}, temos: ',end=' ')
    
    for letra in palvra:
        if letra in vogais:
            print(letra,end=' ')
    print()
       