'''
A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMADOR QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRA
SUA CATEGORIA DE ACORDO COM A IDADE
- ATÉ 9 ANOS: MIRIM
- ATÉ 14 ANOS: INFANTIL
- ATÉ 19 ANOS: JUNIOR
- ATÉ 20 ANOS: SÊNIOR
- ACIMA: MASTER
'''

from datetime import date

data_nascimento = int(input('Digite o ano que você nasceu: \n>'))
data_atual = date.today().year
categoria = data_atual - data_nascimento

#separa as categoria por anos
if categoria > 0 and categoria <= 9:
    print('Sua idade é {} anos, você vai competir na categoria MIRIM'.format(categoria))

elif categoria > 9 and categoria <= 14:
    print('Sua idade é {} anos, você vai competir na categoria INFANTIL'.format(categoria))

elif categoria > 14 and categoria <= 19:
    print('Sua idade é {} anos, você vai competir na categoria JUNIOR'.format(categoria))

elif categoria > 19 and categoria <= 20:
    print('Sua idade é {} anos, você vai competir na categoria SÊNIOR'.format(categoria))

elif categoria > 20:
    print('Sua idade é {} anos, você vai competir na categoria MASTER'.format(categoria))

else:
    print('Sua data esta errada, tende denovo!')