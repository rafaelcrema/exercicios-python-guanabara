'''
FAÇA UM PROGRAMA QUE TENHA UMS FUNÇÃO CHAMADA CONTADOR().
QUE RECEBE TÊS PARÂMETROS: INICIO, FIM E PASSO E REALIZA A CONTAGEM.

SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS ATRAVEZ DA FUNÇÃO CRIADA

[A] DE 1 ATÉ 10 DE 1 EM 1
[B] DE 10 ATÉ 0 DE 2 EM 2
[C] UMA CONTAGEM PERSONALIZADA
'''

print('==='*15)
print('EXERCICIOS 98'.center(45))
print('==='*15)
print(' ')

from time import sleep


def contagem():
    for c in range(0,11):
        print(c,end=' ',flush=True)
        sleep(0.2)

    print('\n----------------------')

    for c in range(10, -1, -1):
        print(c,end=' ', flush=True,)
        sleep(0.2)

    print('\n----------------------')

    print('Agora é sua vez!')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    print('\n----------------------')

    if passo < 0:
        for c in range(inicio,fim,-1):
            print(c,end=' ', flush=True)
            sleep(0.2)

    elif passo == 0:
        for c in range(inicio,fim,1):
            print(c,end=' ', flush=True)
            sleep(0.2)



contagem()