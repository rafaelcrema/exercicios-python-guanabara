'''
faça um programa que tenha uma função chamada escreva()
que recebe um texto qualquer como parametro e mostra uma mensgem com o
tamanho adaptavel
ex:
escreve('Olá mundo')
saida
---------
Olá mundo
---------
'''

print('==='*15)
print('EXERCICIOS 97'.center(45))
print('==='*15)
print(' ')

def escreva(msg):
    tamanho = len(msg)+4
    print('~'*tamanho)
    print(f'  {msg}')
    print('~'*tamanho)


escreva('teste')
escreva('ovo')
escreva('testando o ovo cuzido')
