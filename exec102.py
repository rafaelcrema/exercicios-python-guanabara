'''
CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FATORIAL()
QUE RECEBE DOIS PARAMETROS: O PRIMEIRO QUE INDICA O NÚMERO A CALCULAR E O OUTRO
SHAMA O SHOW, QUE SERÁ UM VALOR LOGICO(OPCIONAL) INDICANDO SE SERÁ MOSTRADO OU NÃO NA TELA 
O PROCESSO DE CALCULO DO FATORIAL
'''

print('==='*15)
print('EXERCICIOS 102'.center(44))
print('==='*15)
print(' ')

#FUNÇÃO
def fatorial(num, show=False):
    '''
    => Calcula o Fatorial de um número.
    Para num: O o numero a ser calculado
    O comando show= é Opcional, para mostrar o funcionlaidade do fatorial
    Return o resultado de num
    '''
    resultado = 1
    multilicador = []
    for f in range(1, num+1):
        resultado *=f
        multilicador.append(f)

    print(resultado)
    print('---'*20)

    if show == True:
        print(num,end='')
        for n in reversed(multilicador):
            print(f' x {n} ',end='')
        
        print(f'= {resultado}')


#CODIGO PRINCIPAL
fatorial(5, show=False)