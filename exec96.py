'''
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA AREA(), QUE RECEBE A IMEÇÃO DE UM TERRENO RETANGULA
(LARGURA E COMPRIMENTO E MOSTRE A AREA DO TERRENO)
'''

print('==='*15)
print('EXERCICIOS 96'.center(45))
print('==='*15)
print(' ')

def area(largura, comprimento):
    return largura * comprimento


print('Contorle de terrenos')
print('--'*10)

largura = float(input('Margura (M): '))
comprimento = float(input('Comprimento (M): '))

print(f'{area(largura, comprimento)} m²')


