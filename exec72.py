'''
CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA COM UMA CONTAGEM POR EXTENSO DE ZERO ATÉ VINTE
SEU PROGRAMA DEVERPA LER UM NÚMERO PELO TECLADO (ENTRE 0 E 20) E MOSTRA-LO POR EXTENSO
'''

print('==='*15)
print('EXERCICIOS 72'.center(45))
print('==='*15)
print(' ')

num_escrito = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
               'doze', 'treze', 'catorza', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

escolha = int(input('Escolha um número entre 1 e 20: \n'))

print('==='*10)

print(f'O número por extenso é:{num_escrito[escolha]}')
