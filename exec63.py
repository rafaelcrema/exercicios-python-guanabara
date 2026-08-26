'''
ESCREVA UM PROGRAMA QUE LEIA UM NUMERO N INTEIRO QUALQUER E MOSTRE NA TELA OS N PRIMEIROS ELEMENTOS DE UMA SEGUENCIA FIBONACC.
EX.: 0,1,1,2,3,5,8
'''

print('==='*15)
print('EXERCICIOS 63'.center(45))
print('==='*15)
print(' ')

num = int(input('Digite o número que você quer saber a seguencia de fibonacci: '))
quantos_num = int(input('Quantos números você quer que a sequencia exiba?'))

antirior = 1
atual = num
proximo = 1

fibonacci = []

contador = 0

while contador < quantos_num:
    fibonacci.append(proximo)
    proximo = antirior + atual

    antirior = atual
    atual = proximo

    contador += 1

print(fibonacci)
