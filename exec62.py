'''
MELHORE O EXERCICIOS 61. PERGUNTANDO PARA O USUARIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS. O PROGRAMA
ENCERRA QUANDO ELE DISSER QUE QUER MOSTRAR 0 TERMOS
'''

print('==='*15)
print('EXERCICIOS 62'.center(45))
print('==='*15)
print(' ')

continuar = 0

while True:

    list_pa = []
    cont = 0

    num = int(input('Digite o número da PA: '))
    razao = int(input('Digite a razao: '))

    term = num
    
    while cont < 10:
        list_pa.append(term)
        term = term + razao
        cont += 1
    print(list_pa)

    pergunta = input('Quer continuar? [S/N]').upper

    if pergunta == 'N':
        break