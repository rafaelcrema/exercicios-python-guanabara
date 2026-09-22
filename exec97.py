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

from time import sleep

texto = ['Olá Mundo', 'teste', 'Você destruiu o meu ovo!']


def escreva():
    for i in texto:
        t = len(i)
        risco = '-' * t
        print(f'{risco}\n{i}\n{risco}')
        print()
        sleep(0.8)
       
escreva()


