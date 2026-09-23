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

def contador(i,f,p):

    if p < 0:
        p *= -1
    
    if p == 0:
        p = 1

    print(f'Contagem de {i} até o {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.2)
            cont += p
        print('FIM')

    else:
        cont = i
        while cont >= f:
            print(cont, end=' ', flush=True)
            sleep(0.2)
            cont -= p
        print('FIM')


contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini,fim,passo)