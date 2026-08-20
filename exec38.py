'''
ESCREVE UM PROGRAMA QUE LIA DOIS NÚMEROS INTEIROS E COMPARE-OS MOSTRANDO NA TELA UMA MENSAGEM:
- O PRIMEIRO NÚMERO É MAIOR
- O SEGUNDO NÚMERO É MAIOR
- NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS
'''
print('-='*30)
print('EXERCICIOS 38')
print('-='*30)

num_1 = int(input('Escolha o primeiro número: \n>'))
num_2 = int(input('Escolha o segundo número: \n>'))

if num_1 > num_2:
    print('O número {} é maior e o {} é menor'.format(num_1, num_2))

elif num_1 < num_2:
    print('O número {} é maior e o {} é menor'.format(num_2, num_1))

else:
    print('Não existe número maior, os dois são iguais')