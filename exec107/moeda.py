'''
AUMENTAR()
DIMINUIR()
DOBRAR()
METADE()
'''

def verifica(p):
    while True:
        try:
            p = p.replace(',', '.')
            return float(p)
        except:
            print('\033[31mErro! Digite um valor valido\033[m')
            p = input('Digite o preço R$ ')
   

def metade(p,form=False):
    valor = p /2
    if form == True:
        valor = f'R$ {valor:.2f}'
    return valor

def dobro(p, form=False):
    valor = p * 2
    if form == True:
        valor = f'R$ {valor:.2f}'
    return valor

def aumento(p, aum):
    return p * aum


def diminuir(p,redu):
    return p * redu
    

def resumo(p,aum = 0,redu = 0):
    p = verifica(p)

    print()
    print('='*45)
    print('RESUMO DO VALOR'.center(45))
    print('='*45)
    print(f'A metade de R$ {p:.2f} é R${metade(p):.>18.2f}')
    print(f'O dobro de R$ {p:.2f} é R${dobro(p):.>18.2f}')

    soma_mais = p * (aum/100)
    total_mais = p + soma_mais
    print(f'Aumentado {aum}%, temos R${total_mais:.>18.2f}')

    soma_menos = p * (redu/100)
    total_menos = p - soma_menos
    print(f'Reduzindo {redu}% temos R$ {total_menos:.>18.2f}')